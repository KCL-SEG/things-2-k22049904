from django.shortcuts import render
from .forms import ThingForm
from django.http import HttpResponse


def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
