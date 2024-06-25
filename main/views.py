from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

def home(request):
    return render(request, 'home.html', {})

@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'profile_list.html', {"profiles": profiles})

@login_required
def profile(request, pk):
    profile = get_object_or_404(Profile, user_id=pk)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def follow_unfollow(request, pk):
    profile = get_object_or_404(Profile, user_id=pk)
    if request.method == 'POST':
        if 'follow' in request.POST:  
            if request.POST['follow'] == 'follow':
                request.user.profile.follows.add(profile)
                messages.success(request, f"You are now following {profile.user.username}.")
            elif request.POST['follow'] == 'unfollow':
                request.user.profile.follows.remove(profile)
                messages.success(request, f"You have unfollowed {profile.user.username}.")
        return redirect('profile', pk=pk)
