from django.db.models import Count, Exists, OuterRef
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Experience, Skill
from main.permissions import (
    IsPortfolioOwnerOrEditorOrReadOnly,
    IsPortfolioOwnerOrReadOnly,
)
from main.serializers import ExperienceSerializer, SkillSerializer


def annotate_stars(queryset, request, model):
    """Tambahkan star_count dan (untuk user login) is_starred."""
    owner = model._meta.model_name          # "skill" / "experience"
    if request.user.is_authenticated:
        mine = model.starred_by.through.objects.filter(user_id=request.user.pk)
        queryset = queryset.annotate(
            is_starred=Exists(mine.filter(**{owner: OuterRef("pk")}))
        )
    return queryset.annotate(star_count=Count("starred_by"))


def build_queryset(request, model):
    user = request.user
    params = request.query_params
    owner = model._meta.model_name
    queryset = model.objects.all()

    title = params.get("title", "").strip()
    if title:
        queryset = queryset.filter(title__icontains=title)

    category = params.get("category", "").strip()
    if category:
        queryset = queryset.filter(category=category)

    if params.get("starred") == "1":
        if user.is_authenticated:
            mine = model.starred_by.through.objects.filter(user_id=user.pk)
            queryset = queryset.filter(pk__in=mine.values(owner))
        else:
            queryset = queryset.none()

    return annotate_stars(queryset, request, model).order_by("title", "id")


def _list_or_create(request, model, serializer_class):
    context = {"request": request}
    if request.method in ("GET", "HEAD"):
        serializer = serializer_class(build_queryset(request, model), many=True, context=context)
        return Response(serializer.data)

    serializer = serializer_class(data=request.data, context=context)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


def _detail(request, pk, model, serializer_class):
    instance = get_object_or_404(annotate_stars(model.objects.all(), request, model), pk=pk)
    context = {"request": request}

    if request.method in ("GET", "HEAD"):
        return Response(serializer_class(instance, context=context).data)

    if request.method == "DELETE":
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = serializer_class(
        instance,
        data=request.data,
        partial=(request.method == "PATCH"),
        context=context,
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


def _toggle_star(request, pk, model, serializer_class):
    instance = get_object_or_404(model, pk=pk)
    if instance.starred_by.filter(pk=request.user.pk).exists():
        instance.starred_by.remove(request.user)
    else:
        instance.starred_by.add(request.user)
    # Ambil ulang supaya star_count dan is_starred (annotate) sudah yang terbaru.
    instance = get_object_or_404(annotate_stars(model.objects.all(), request, model), pk=pk)
    return Response(serializer_class(instance, context={"request": request}).data)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def experience_list(request):
    return _list_or_create(request, Experience, ExperienceSerializer)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly(Experience)])
def experience_detail(request, pk):
    return _detail(request, pk, Experience, ExperienceSerializer)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def skill_list(request):
    return _list_or_create(request, Skill, SkillSerializer)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly(Skill)])
def skill_detail(request, pk):
    return _detail(request, pk, Skill, SkillSerializer)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def experience_star(request, pk):
    return _toggle_star(request, pk, Experience, ExperienceSerializer)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def skill_star(request, pk):
    return _toggle_star(request, pk, Skill, SkillSerializer)