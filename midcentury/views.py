from django.shortcuts import render
from midcentury.models import Collection


def index_view(request):
    return render(request, "index.html", {})


def about_me(request):
    return render(request, "aboutme.html", {})


def collection(request):
    vintage_ads = Collection.objects.all()
    return render(request, "collection.html", {"ads": vintage_ads})