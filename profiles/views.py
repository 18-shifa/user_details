# profiles/views.py
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    user_profile = request.user.userprofile
    return render(request, 'profiles/profile.html', {'user_profile': user_profile, 'edit_mode': False})

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profiles/profile.html', {'form': form, 'edit_mode': True})
