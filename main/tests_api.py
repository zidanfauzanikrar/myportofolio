import uuid

from django.contrib.auth.models import Group, User
from django.db import connection
from django.test.utils import CaptureQueriesContext
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.models import Experience, Skill


class PortfolioAPITestMixin:
    """Test yang sama dijalankan untuk Skill dan Experience.

    Subclass wajib mengisi: model, route, page_url_name, create_kwargs,
    payload, other_category, invalid_changes. Akun hanya data uji di database
    pengujian, bukan akun produksi.
    """

    model = None
    route = None
    page_url_name = None
    create_kwargs = {}
    payload = {}
    other_category = ""
    invalid_changes = []

    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner", password="test-password", email="owner@example.com",
        )
        self.visitor = User.objects.create_user(username="visitor", password="test-password")
        self.obj = self.model.objects.create(**self.create_kwargs)
        self.list_url = reverse(f"api:{self.route}-list")
        self.detail_url = reverse(f"api:{self.route}-detail", args=[self.obj.id])
        self.star_url = reverse(f"api:{self.route}-star", args=[self.obj.id])

    def make_editor(self):
        # Group "Editor" dibuat oleh migrasi 0004 (izin change_*, tanpa add/delete).
        self.visitor.groups.add(Group.objects.get(name="Editor"))

    def make_extra(self, **changes):
        return self.model.objects.create(**{**self.create_kwargs, **changes})

    # ---------- baca (publik) ----------

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], str(self.obj.id))
        self.assertFalse(response.data[0]["is_starred"])
        self.assertEqual(response.data[0]["star_count"], 0)
        self.assertNotIn("fields", response.data[0])
        self.assertEqual(self.client.get(self.detail_url).status_code, status.HTTP_200_OK)

    def test_search_category_and_empty_results(self):
        self.make_extra(title="Other item", category=self.other_category)
        response = self.client.get(self.list_url, {"title": "OTHER"})
        self.assertEqual(len(response.data), 1)
        response = self.client.get(self.list_url, {"category": self.other_category})
        self.assertEqual([item["title"] for item in response.data], ["Other item"])
        response = self.client.get(self.list_url, {"title": "not-found"})
        self.assertEqual(response.data, [])

    def test_missing_item(self):
        url = reverse(f"api:{self.route}-detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_list_query_count_is_constant(self):
        self.client.force_authenticate(user=self.visitor)
        with CaptureQueriesContext(connection) as small:
            self.client.get(self.list_url)
        for index in range(5):
            self.make_extra(title=f"Extra {index}")
        with CaptureQueriesContext(connection) as large:
            response = self.client.get(self.list_url)
        self.assertEqual(len(response.data), 6)
        self.assertEqual(len(small), len(large))

    # ---------- izin tulis ----------

    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.patch(self.detail_url, {"title": "Changed"}, format="json").status_code, 403)
            self.assertEqual(self.client.put(self.detail_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(self.model.objects.count(), 1)
        self.obj.refresh_from_db()
        self.assertEqual(self.obj.title, self.create_kwargs["title"])

    def test_staff_without_permission_cannot_update(self):
        self.visitor.is_staff = True
        self.visitor.save()
        self.client.force_authenticate(user=self.visitor)
        response = self.client.patch(self.detail_url, {"title": "Changed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_editor_can_update_but_not_create_or_delete(self):
        self.make_editor()
        self.client.force_authenticate(user=self.visitor)
        response = self.client.patch(self.detail_url, {"title": "Edited"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Edited")
        response = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.client.post(self.list_url, self.payload, format="json").status_code,
            status.HTTP_403_FORBIDDEN,
        )
        self.assertEqual(self.client.delete(self.detail_url).status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(self.model.objects.filter(pk=self.obj.id).exists())
        self.assertEqual(self.model.objects.count(), 1)

    # ---------- create, validasi, update, delete ----------

    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(self.model.objects.filter(pk=response.data["id"]).exists())
        self.assertEqual(response.data["title"], self.payload["title"])

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)
        for changes, field in self.invalid_changes:
            with self.subTest(field=field, changes=changes):
                response = self.client.post(self.list_url, {**self.payload, **changes}, format="json")
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertIn(field, response.data)
        self.assertEqual(self.model.objects.count(), 1)

    def test_html_tags_are_stripped_from_text(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(
            self.list_url,
            {**self.payload, "title": "<b>Bold</b> title", "description": "<script>x</script>Text"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotIn("<", response.data["title"])
        self.assertNotIn("<", response.data["description"])

    def test_patch_put_and_delete(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.detail_url, {"title": "Changed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.obj.refresh_from_db()
        self.assertEqual(self.obj.title, "Changed")
        self.assertEqual(self.obj.description, self.create_kwargs["description"])
        response = self.client.put(self.detail_url, {"title": "Incomplete"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.payload["title"])
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")
        self.assertFalse(self.model.objects.filter(pk=self.obj.id).exists())

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload, "star_count": 99, "is_starred": True,
            "category_display": "forged", "starred_by": [self.visitor.id],
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])
        self.assertNotEqual(response.data["category_display"], "forged")

    def test_wrong_method(self):
        self.client.force_authenticate(user=self.owner)
        self.assertEqual(self.client.delete(self.list_url).status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # ---------- star ----------

    def test_star_requires_login_and_toggles(self):
        self.assertEqual(self.client.post(self.star_url).status_code, status.HTTP_403_FORBIDDEN)
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)
        response = self.client.post(self.star_url)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)

    def test_star_missing_item(self):
        self.client.force_authenticate(user=self.visitor)
        url = reverse(f"api:{self.route}-star", args=[uuid.uuid4()])
        self.assertEqual(self.client.post(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_star_get_is_not_allowed(self):
        self.client.force_authenticate(user=self.visitor)
        self.assertEqual(self.client.get(self.star_url).status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_starred_filter_keeps_star_count_correct(self):
        other = self.make_extra(title="Not starred")
        self.obj.starred_by.add(self.owner, self.visitor)
        self.client.force_authenticate(user=self.visitor)
        response = self.client.get(self.list_url, {"starred": "1"})
        self.assertEqual([item["id"] for item in response.data], [str(self.obj.id)])
        self.assertEqual(response.data[0]["star_count"], 2)
        self.assertTrue(response.data[0]["is_starred"])
        response = self.client.get(self.list_url)
        by_id = {item["id"]: item for item in response.data}
        self.assertFalse(by_id[str(other.id)]["is_starred"])

    def test_guest_starred_filter_is_empty(self):
        self.obj.starred_by.add(self.visitor)
        response = self.client.get(self.list_url, {"starred": "1"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_usernames_do_not_leak(self):
        self.obj.starred_by.add(self.visitor, self.owner)
        self.client.force_authenticate(user=self.visitor)
        for url in (self.list_url, self.detail_url):
            body = self.client.get(url).content.decode()
            self.assertNotIn("visitor", body)
            self.assertNotIn("owner", body)

    # ---------- empat peran dan metode aman ----------

    def snapshot(self):
        return (
            list(self.model.objects.order_by("pk").values()),
            self.model.starred_by.through.objects.count(),
        )

    def test_get_and_options_never_change_data(self):
        self.make_editor()
        before = self.snapshot()
        for user in (None, self.visitor, self.owner):
            self.client.force_authenticate(user=user)
            for url in (self.list_url, self.detail_url):
                with self.subTest(user=getattr(user, "username", "guest"), url=url):
                    self.assertEqual(self.client.get(url).status_code, status.HTTP_200_OK)
                    self.assertEqual(self.client.options(url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.snapshot(), before)

    def test_four_roles(self):
        # 1. Pengunjung (belum login): hanya membaca.
        self.client.force_authenticate(user=None)
        self.assertEqual(self.client.get(self.list_url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.get(self.detail_url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.post(self.star_url).status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.client.patch(self.detail_url, {"title": "X"}, format="json").status_code, 403)

        # 2. Pengguna biasa: membaca dan star, tidak bisa menulis.
        regular = User.objects.create_user(username="regular", password="test-password")
        self.client.force_authenticate(user=regular)
        self.assertEqual(self.client.get(self.list_url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.post(self.star_url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.patch(self.detail_url, {"title": "X"}, format="json").status_code, 403)
        self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)

        # 3. Editor: juga bisa PUT/PATCH, tetapi tidak create/delete.
        self.make_editor()
        self.client.force_authenticate(user=self.visitor)
        self.assertEqual(self.client.post(self.star_url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.patch(self.detail_url, {"title": "Editor edit"}, format="json").status_code, 200)
        self.assertEqual(self.client.put(self.detail_url, self.payload, format="json").status_code, 200)
        self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)

        # 4. Pemilik: semuanya, termasuk create dan delete.
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.client.delete(self.detail_url).status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.model.objects.count(), 1)

    # ---------- CSRF (autentikasi sesi) ----------

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.model.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)
        client.login(username="owner", password="test-password")
        # Halaman daftar merender {{ csrf_token }}, sehingga cookie csrftoken dibuat.
        page = client.get(reverse(self.page_url_name))
        self.assertEqual(page.status_code, status.HTTP_200_OK)
        token = client.cookies["csrftoken"].value
        response = client.post(
            self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = client.patch(
            self.detail_url, {"title": "Via session"}, format="json", HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = client.post(self.star_url, HTTP_X_CSRFTOKEN=token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SkillAPITest(PortfolioAPITestMixin, APITestCase):
    model = Skill
    route = "skill"
    page_url_name = "main:show_skill"
    create_kwargs = {
        "title": "Python", "description": "Backend scripting",
        "category": "programming_language",
    }
    payload = {
        "title": "Django", "description": "Web framework", "category": "hard_skill",
    }
    other_category = "soft_skill"
    invalid_changes = [
        ({"title": "   "}, "title"),
        ({"title": '<img src="x" onerror="alert(1)">'}, "title"),
        ({"description": "<b></b>"}, "description"),
        ({"category": "not-a-category"}, "category"),
    ]


class ExperienceAPITest(PortfolioAPITestMixin, APITestCase):
    model = Experience
    route = "experience"
    page_url_name = "main:show_experience"
    create_kwargs = {
        "title": "Backend Intern", "description": "Built REST APIs",
        "category": "internship",
    }
    payload = {
        "title": "Research Assistant", "description": "Machine learning lab",
        "category": "research", "thumbnail": "https://example.com/thumb.png",
        "ended_at": None,
    }
    other_category = "volunteer"
    invalid_changes = [
        ({"title": "   "}, "title"),
        ({"title": '<img src="x" onerror="alert(1)">'}, "title"),
        ({"description": "<b></b>"}, "description"),
        ({"category": "not-a-category"}, "category"),
        ({"thumbnail": "javascript:alert(1)"}, "thumbnail"),
    ]

    def test_started_at_and_is_ongoing_are_read_only(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload, "started_at": "2000-01-01T00:00:00Z", "is_ongoing": False,
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(response.data["started_at"].startswith("2000"))
        self.assertTrue(response.data["is_ongoing"])

    def test_ended_at_controls_is_ongoing(self):
        self.client.force_authenticate(user=self.owner)
        self.assertTrue(self.client.get(self.detail_url).data["is_ongoing"])
        # Format yang dikirim modal edit: tanggal + T00:00:00
        response = self.client.patch(
            self.detail_url, {"ended_at": "2026-10-30T00:00:00"}, format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data["is_ongoing"])
        response = self.client.patch(self.detail_url, {"ended_at": None}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["is_ongoing"])

    def test_empty_thumbnail_is_stored_as_null(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.detail_url, {"thumbnail": None}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNone(response.data["thumbnail"])