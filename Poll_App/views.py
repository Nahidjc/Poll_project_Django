from django.shortcuts import render
from .forms import CreatePollForm
from .models import Poll
# Create your views here.


def home(request):
    return render(request, 'poll/home.html', context={})


def create(request):
    form = CreatePollForm()
    return render(request, 'poll/create.html', context={'form': form})


def vote(request, poll_id):
    return render(request, 'poll/vote.html', context={})


def results(request, poll_id):
    return render(request, 'poll/results.html', context={})
