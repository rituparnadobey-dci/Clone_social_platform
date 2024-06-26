from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, MainPost
from .forms import MainPostForm

def home(request):
    if request.user.is_authenticated:
        form = MainPostForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success (request, ("Your Post is public now."))
                return redirect('home')

        post = MainPost.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"posts":post, "form":form})
    else:
        post = MainPost.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"posts":post})

@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'profile_list.html', {"profiles": profiles})

@login_required
def profile(request, pk):
    profile = get_object_or_404(Profile, user_id=pk)
    posts = MainPost.objects.filter(user_id=pk)
    return render(request, 'profile.html', {'profile': profile, "posts":posts })

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
