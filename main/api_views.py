from django.db.models import Count, Exists, OuterRef
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from main.models import Experience, Skill
from main.permissions import IsPortfolioOwnerOrReadOnly
from main.serializers import ExperienceSerializer, SkillSerializer


def build_queryset(request, model):
    user = request.user
    params = request.query_params
    through = model.starred_by.through
    owner = model._meta.model_name          # "skill" / "experience"
    queryset = model.objects.all()

    title = params.get("title", "").strip()
    if title:
        queryset = queryset.filter(title__icontains=title)

    category = params.get("category", "").strip()
    if category:
        queryset = queryset.filter(category=category)

    starred_only = params.get("starred") == "1"
    if user.is_authenticated:
        mine = through.objects.filter(user_id=user.pk)
        if starred_only:
            queryset = queryset.filter(pk__in=mine.values(owner))
        queryset = queryset.annotate(
            is_starred=Exists(mine.filter(**{owner: OuterRef("pk")}))
        )
    elif starred_only:
        queryset = queryset.none()

    return queryset.annotate(star_count=Count("starred_by")).order_by("title", "id")


def _list_or_create(request, model, serializer_class):
    context = {"request": request}
    if request.method in ("GET", "HEAD"):
        serializer = serializer_class(build_queryset(request, model), many=True, context=context)
        return Response(serializer.data)

    serializer = serializer_class(data=request.data, context=context)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def experience_list(request):
    return _list_or_create(request, Experience, ExperienceSerializer)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def skill_list(request):
    return _list_or_create(request, Skill, SkillSerializer)