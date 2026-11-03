from django.urls import path
from main.api_views import experience_list, skill_list

app_name = "api"
urlpatterns = [
    path("experience/", experience_list, name="experience-list"),
    path("skills/", skill_list, name="skill_list"),
]