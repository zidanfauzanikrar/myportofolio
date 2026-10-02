from django.contrib import messages
from django.core import serializers
from django.db.models.aggregates import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST

from main.models import Experience, Skill
from main.forms import ExperienceForm, SkillForm

import datetime

name = "Zidan Fauzan Ikrar"


# Register and Login

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": name,
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": name,
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


# Main

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": name,
        "npm": "2506589616",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Third term CS student at Universitas Indonesia. Dedicated to learn "
            "and delve into Machine Learning (ML) & AI."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


# Experience

def show_experience(request):
    context = {
        "name": name,
        "title_query": request.GET.get("title", "").strip(),
        "category_query": request.GET.get("category", "").strip(),
        "starred_query": request.GET.get("starred", "") == "1",
        "category_choices": Experience.EXPERIENCE_CHOICES,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": name,
        "form": form,
    }
    return render(request, "experience_form.html", context)

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pengalaman."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Pengalaman berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

def show_experience(request):
    context = {
        "name": name,
        "title_query": request.GET.get("title", "").strip(),
        "category_query": request.GET.get("category", "").strip(),
        "starred_query": request.GET.get("starred", "") == "1",
        "category_choices": Experience.EXPERIENCE_CHOICES,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)


def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    category_query = request.GET.get("category", "").strip()
    starred_only = request.GET.get("starred", "") == "1"
    experiences = Experience.objects.all()

    starred_ids = set()
    if request.user.is_authenticated:
        starred_ids = set(request.user.starred_experience.values_list("pk", flat=True))

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    if category_query:
        experiences = experiences.filter(category=category_query)

    if starred_only:
        experiences = experiences.filter(pk__in=starred_ids)

    experiences = experiences.annotate(star_count=Count("starred_by"))

    data = []
    for experience in experiences:
        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "category_display": experience.get_category_display(),
                "thumbnail": experience.thumbnail,
                "started_at": experience.started_at,
                "ended_at": experience.ended_at,
                "is_ongoing": experience.is_ongoing,
                "star_count": experience.star_count,
                "is_starred": experience.pk in starred_ids,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.has_perm("main.change_experience"):
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": name,
        "form": form,
        "is_edit": True,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def toggle_experience_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

# Skill

def show_skill(request):
    context = {
        "name": name,
        "title_query": request.GET.get("title", "").strip(),
        "category_query": request.GET.get("category", "").strip(),
        "starred_query": request.GET.get("starred", "") == "1",
        "category_choices": Skill.SKILL_CHOICES,
        "form": SkillForm(),
    }
    return render(request, "skill.html", context)

@login_required(login_url="/login/")
def create_skill(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = SkillForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill baru berhasil ditambahkan!")
        return redirect("main:show_skill")

    context = {
        "name": name,
        "form": form,
    }
    return render(request, "skill_form.html", context)

@require_POST
def create_skill_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan skill."},
            status=403,
        )

    form = SkillForm(request.POST)
    if form.is_valid():
        skill = form.save()
        return JsonResponse(
            {"message": "Skill berhasil ditambahkan.", "pk": str(skill.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

def get_skill_json(request):
    title_query = request.GET.get("title", "").strip()
    category_query = request.GET.get("category", "").strip()
    starred_only = request.GET.get("starred", "") == "1"
    skills = Skill.objects.all()

    starred_ids = set()
    if request.user.is_authenticated:
        starred_ids = set(request.user.starred_skill.values_list("pk", flat=True))

    if title_query:
        skills = skills.filter(title__icontains=title_query)

    if category_query:
        skills = skills.filter(category=category_query)

    if starred_only:
        skills = skills.filter(pk__in=starred_ids)

    skills = skills.annotate(star_count=Count("starred_by"))

    data = []
    for skill in skills:
        data.append({
            "pk": str(skill.id),
            "fields": {
                "title": skill.title,
                "description": skill.description,
                "category": skill.category,
                "category_display": skill.get_category_display(),
                "star_count": skill.star_count,
                "is_starred": skill.pk in starred_ids,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_skill(request, skill_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")
        return redirect("main:show_skill")

    return redirect("main:show_skill")

@login_required(login_url="/login/")
def update_skill(request, skill_id):
    if not request.user.has_perm("main.change_skill"):
        raise PermissionDenied
    skill = get_object_or_404(Skill, pk=skill_id)
    form = SkillForm(request.POST or None, instance=skill)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill berhasil diperbarui!")
        return redirect("main:show_skill")

    context = {
        "name": name,
        "form": form,
        "is_edit": True,
    }
    return render(request, "skill_form.html", context)

@login_required(login_url="/login/")
def toggle_skill_star(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        if request.user in skill.starred_by.all():
            skill.starred_by.remove(request.user)
        else:
            skill.starred_by.add(request.user)

    return redirect("main:show_skill")

# Custom Permission Denied

def custom_permission_denied(request, exception=None):
    return render(request, "403.html", {"name": name}, status=403)