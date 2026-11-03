from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience, Skill


class PortfolioItemMixin:
    """Validasi teks dan field star yang dipakai bersama oleh Skill dan Experience."""

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Judul tidak boleh kosong atau hanya berisi tag HTML."
            )
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Deskripsi tidak boleh kosong atau hanya berisi tag HTML."
            )
        return value

    def get_star_count(self, obj):
        annotated = getattr(obj, "star_count", None)
        if annotated is not None:
            return annotated
        return obj.starred_by.count()
    
    def get_is_starred(self, obj):
        annotated = getattr(obj, "is_starred", None)
        if annotated is not None:
            return annotated
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return obj.starred_by.filter(pk=request.user.pk).exists()


class SkillSerializer(PortfolioItemMixin, serializers.ModelSerializer):
    category_display = serializers.CharField(
        source="get_category_display", read_only=True
    )
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = [
            "id", "title", "description",
            "category", "category_display",
            "star_count", "is_starred",
        ]
        read_only_fields = ["id"]


class ExperienceSerializer(PortfolioItemMixin, serializers.ModelSerializer):
    category_display = serializers.CharField(
        source="get_category_display", read_only=True
    )
    is_ongoing = serializers.BooleanField(read_only=True)
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description",
            "category", "category_display",
            "thumbnail", "started_at", "ended_at", "is_ongoing",
            "star_count", "is_starred",
        ]
        read_only_fields = ["id", "started_at"]