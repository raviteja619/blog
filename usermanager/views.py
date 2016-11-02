from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib import messages


def home(request):
    """Main Homepage."""
    return render(request, 'index.html')


def register(request):
    """Register method."""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save(**data)
            user = authenticate(username=data['username'], password=data['password1'])
            if user:
                login(request, user)
            return HttpResponseRedirect('/')
        else:
            print form.errors
            messages.error(request, form.errors)

    else:
        form = RegistrationForm()
    ctx = {'form': form}

    return render(request, 'register.html', ctx)
