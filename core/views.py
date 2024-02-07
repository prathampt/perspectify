from django.shortcuts import render, redirect
from django.contrib.auth import logout as user_logout


from .forms import SignupForm


def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/core/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout(request):
    user_logout(request)
    return redirect('/core/login/')

def profile(request):
    return render(request, 'core/profile.html', {'user_profile': request.user})