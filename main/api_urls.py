from django.urls import path
from rest_framework.authtoken import views as authtoken_views

from main import api_views

app_name = "api"

urlpatterns = [
    path("auth/token/", authtoken_views.obtain_auth_token, name="api_token_auth"),
    path("auth/logout/", api_views.api_logout, name="api_logout"),

    path("experience/", api_views.experience_list, name="experience-list"),
    path("experience/<uuid:pk>/", api_views.experience_detail, name="experience-detail"),
    path("experience/<uuid:pk>/star/", api_views.experience_star, name="experience-star"),

    path("skills/", api_views.skill_list, name="skill-list"),
    path("skills/<uuid:pk>/", api_views.skill_detail, name="skill-detail"),
    path("skills/<uuid:pk>/star/", api_views.skill_star, name="skill-star"),
]