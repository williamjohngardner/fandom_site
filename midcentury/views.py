from django.shortcuts import render


def index_view(request):
    return render(request, "index.html", {})


def about_me(request):
    return render(request, "aboutme.html", {})


def collection(request):
    return render(request, "collection.html", {})