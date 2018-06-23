from django.shortcuts import render, redirect

import data.models
import data.forms


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, "main_page/index.html", {"username": username})

    else:
        return render(request, "main_page/index.html")


def redirect_to_index(request):
    return redirect(to="/index")


def display_events(request):
    events = [data.forms.BriefEventForm(instance=i) for i in data.models.Event.objects.all()]

    return render(request, "main_page/events.html", {"events": events})
