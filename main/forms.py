from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Skill, Experience

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            "title",
            "description",
            "category",
        ]

        labels = {
            "title": "Nama Skill",
            "description": "Deskripsi Skill",
            "category": "Kategori Skill",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Tuliskan Keahlianmu",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsikan Keahlianmu",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "Language, Programming Language, Soft-skill, Hard-skill",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Nama Experience",
            "description": "Deskripsi Experience",
            "category": "Kategori Experience",
            "thumbnail": "Thumbnail",
            "ended_at": "Tanggal Selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Tuliskan Keahlianmu",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsikan Keahlianmu",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "Internship, Research, Volunteer, Part-time, Full-time, Freelance",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "ended_at": TextInput(
                attrs={
                    "type": "date",
                    "placeholder": "Kosongkan jika masih berlangsung",
                }
            ),
        }