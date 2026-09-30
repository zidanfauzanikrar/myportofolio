from django.forms import ModelForm, TextInput, Textarea, URLInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

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
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama skill tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"]).strip()
        if not description:
            raise ValidationError("Deskripsi tidak boleh hanya berisi tag HTML.")
        return description

    def clean_category(self):
        return strip_tags(self.cleaned_data["category"]).strip()

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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama pengalaman tidak boleh hanya berisi tag HTML.")
        return title
    
    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

    def clean_category(self):
        return strip_tags(self.cleaned_data["category"]).strip()