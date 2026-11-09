from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Skill


class MainStatsTest(TestCase):
    def setUp(self):
        self.url = reverse("main:show_main")

    def make_skill(self, title, category="hard_skill"):
        return Skill.objects.create(title=title, description="desc", category=category)

    def make_experience(self, title, ended=False):
        return Experience.objects.create(
            title=title,
            description="desc",
            category="internship",
            ended_at=timezone.now() if ended else None,
        )

    def test_empty_database(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        stats = response.context["stats"]
        self.assertEqual(stats["skill_count"], 0)
        self.assertEqual(stats["experience_count"], 0)
        self.assertEqual(stats["ongoing_count"], 0)
        self.assertEqual(stats["total_stars"], 0)
        self.assertIsNone(stats["top_skill"])
        self.assertIsNone(stats["top_experience"])
        self.assertContains(response, "Statistik Portofolio")
        self.assertContains(response, "Belum ada star")

    def test_counts_and_top_items(self):
        first = User.objects.create_user(username="first", password="x")
        second = User.objects.create_user(username="second", password="x")
        popular = self.make_skill("Python")
        quiet = self.make_skill("Django")
        self.make_skill("Unstarred")
        popular.starred_by.add(first, second)
        quiet.starred_by.add(first)
        ongoing = self.make_experience("Mentor")
        self.make_experience("Intern", ended=True)
        self.make_experience("Assistant", ended=True)
        ongoing.starred_by.add(first)

        stats = self.client.get(self.url).context["stats"]
        self.assertEqual(stats["skill_count"], 3)
        self.assertEqual(stats["experience_count"], 3)
        self.assertEqual(stats["ongoing_count"], 1)
        self.assertEqual(stats["total_stars"], 4)
        self.assertEqual(stats["top_skill"].title, "Python")
        self.assertEqual(stats["top_skill"].star_count, 2)
        self.assertEqual(stats["top_experience"].title, "Mentor")

    def test_tie_is_broken_by_title(self):
        user = User.objects.create_user(username="voter", password="x")
        for title in ("Zebra", "Alpha"):
            self.make_skill(title).starred_by.add(user)
        stats = self.client.get(self.url).context["stats"]
        self.assertEqual(stats["top_skill"].title, "Alpha")

    def test_stats_are_public_and_do_not_leak_usernames(self):
        user = User.objects.create_user(username="secret-user", password="x")
        self.make_skill("Python").starred_by.add(user)
        response = self.client.get(self.url)  # tanpa login
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "secret-user")
        self.assertContains(response, "Python")

    def test_titles_are_escaped(self):
        user = User.objects.create_user(username="voter", password="x")
        self.make_skill("<script>alert(1)</script>").starred_by.add(user)
        response = self.client.get(self.url)
        self.assertNotContains(response, "<script>alert(1)</script>")
        self.assertContains(response, "&lt;script&gt;")