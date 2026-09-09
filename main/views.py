from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Zidan Fauzan Ikrar",
        "npm": "2506589616",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Third term CS student at Universitas Indonesia. Dedicated to learn "
            "and delve into Machine Learning (ML) & AI."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Zidan Fauzan Ikrar",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)