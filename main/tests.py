from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Skill


class MainTest(TestCase):
    """Test halaman dan model.

    Sejak Week 5 halaman Experience dan Skill hanya berupa kerangka HTML; daftar
    datanya diambil lewat fetch() ke API (/api/v1/...). Karena itu isi data
    dites lewat endpoint API, sedangkan halamannya dites untuk kerangka,
    elemen penting, dan alamat endpoint yang dipakai script.
    """

    def setUp(self):
        self.experience = Experience.objects.create(
            title="PBP Teaching Assistant",
            description="Help students understand web development.",
            category="part-time",
        )
        self.skill = Skill.objects.create(
            title="Communication",
            description="Gives and receives information clearly, listens actively, and adapt messages to different audiences",
            category="soft_skill",
        )

    # ---------- halaman utama ----------

    def test_main_url_is_accessible_experience(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_main_url_is_accessible_skill(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.skill.title)
        self.assertContains(response, f'href="{reverse("main:show_skill")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/a-page-that-does-not-exist/")

        self.assertEqual(response.status_code, 404)

    # ---------- Experience ----------

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "PBP Teaching Assistant")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        # Kerangka halaman: data tidak dirender di server, dimuat lewat AJAX.
        self.assertNotContains(response, self.experience.title)
        self.assertNotContains(response, self.experience.description)
        for element_id in ("loading", "error", "empty", "grid"):
            self.assertContains(response, f'id="{element_id}"')
        # Dropdown kategori diisi dari EXPERIENCE_CHOICES.
        self.assertContains(response, "Part-Time")
        # Script memakai endpoint API.
        self.assertContains(response, reverse("api:experience-list"))
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_experience_api_returns_data(self):
        response = self.client.get(reverse("api:experience-list"))

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["id"], str(self.experience.id))
        self.assertEqual(data[0]["title"], self.experience.title)
        self.assertEqual(data[0]["description"], self.experience.description)
        self.assertEqual(data[0]["category"], "part-time")
        self.assertEqual(data[0]["category_display"], "Part-Time")
        self.assertTrue(data[0]["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        page = self.client.get(reverse("main:show_experience"))
        api = self.client.get(reverse("api:experience-list"))

        # Pesan kosong ada di kerangka halaman dan ditampilkan script saat API membalas [].
        self.assertContains(page, "Belum ada experience yang ditambahkan atau ditemukan.")
        self.assertEqual(api.status_code, 200)
        self.assertEqual(api.json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("api:experience-list"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertFalse(response.json()[0]["is_ongoing"])
        self.assertIsNotNone(response.json()[0]["ended_at"])

    # ---------- Skill ----------

    def test_skill_model(self):
        self.assertEqual(str(self.skill), "Communication")
        self.assertEqual(self.skill.category, "soft_skill")

    def test_skill_page(self):
        response = self.client.get(reverse("main:show_skill"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        self.assertNotContains(response, self.skill.title)
        self.assertNotContains(response, self.skill.description)
        for element_id in ("loading", "error", "empty", "grid"):
            self.assertContains(response, f'id="{element_id}"')
        # Dropdown kategori diisi dari SKILL_CHOICES.
        self.assertContains(response, "Soft-skill")
        self.assertContains(response, reverse("api:skill-list"))
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_skill_api_returns_data(self):
        response = self.client.get(reverse("api:skill-list"))

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["id"], str(self.skill.id))
        self.assertEqual(data[0]["title"], self.skill.title)
        self.assertEqual(data[0]["description"], self.skill.description)
        self.assertEqual(data[0]["category"], "soft_skill")
        self.assertEqual(data[0]["category_display"], "Soft-skill")

    def test_empty_skill_page(self):
        Skill.objects.all().delete()
        page = self.client.get(reverse("main:show_skill"))
        api = self.client.get(reverse("api:skill-list"))

        self.assertContains(page, "Belum ada skill yang ditambahkan atau ditemukan.")
        self.assertEqual(api.status_code, 200)
        self.assertEqual(api.json(), [])