from django.shortcuts import render, redirect
from .forms import MediaItemForm
from .models import MediaItem


def home(request):
    items = MediaItem.objects.order_by("-uploaded_at")
    return render(request, "gallery/home.html", {"items": items})


def upload(request):
    if request.method == "POST":
        form = MediaItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MediaItemForm()
    return render(request, "gallery/upload.html", {"form": form})
