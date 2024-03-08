from django.shortcuts import render, redirect
from django.contrib.auth import logout as user_logout
from .models import UserProfile

from .forms import SignupForm

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def privacyPolicy(request):
    return render(request, 'core/privacyPolicy.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            # Save the User object
            user = form.save()

            # Create UserProfile instance and associate it with the User
            user_profile = user.userprofile
            user_profile.name = form.cleaned_data['name']
            user_profile.username = form.cleaned_data['username']
            user_profile.email = form.cleaned_data['email']
            user_profile.interests = form.cleaned_data['interests']
            user_profile.about_me = form.cleaned_data['about_me']
            user_profile.language = form.cleaned_data['language']
            user_profile.save()

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
    user_profile = UserProfile.objects.get(user=request.user)
    print(user_profile)
    return render(request, 'core/profile.html', {'user_profile': user_profile})