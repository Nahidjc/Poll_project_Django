from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll
# Create your views here.


def home(request):
    return render(request, 'poll/home.html', context={})


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()

    return render(request, 'poll/create.html', context={'form': form})


def vote(request, poll_id):
    return render(request, 'poll/vote.html', context={})


def results(request, poll_id):
    return render(request, 'poll/results.html', context={})
