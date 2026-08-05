from django.shortcuts import render, redirect
from .models import Thought


def home(request):
    if request.method == "POST":
        content = request.POST.get("content")

        if content:
            Thought.objects.create(content=content)

        return redirect("home")

    thoughts = Thought.objects.all().order_by("-created_at")

    return render(
        request,
        "thoughts/home.html",
        {
            "thoughts": thoughts
        },
    )