from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile, MainPost
from .forms import MainPostForm, SignUpForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated:
        form = MainPostForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, "Your post is now public.")
                return redirect('home')
        posts = MainPost.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"posts": posts, "form": form})
    else:
        posts = MainPost.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"posts": posts})




@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'profile_list.html', {"profiles": profiles})




@login_required
def profile(request, pk):
    profile = get_object_or_404(Profile, user_id=pk)
    posts = MainPost.objects.filter(user_id=pk)
    return render(request, 'profile.html', {'profile': profile, "posts": posts})



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



    
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            # Authenticate and login the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been registered and logged in.")
                return redirect('home')
            else:
                messages.error(request, "Registration successful but login failed. Please try logging in manually.")
                return redirect('login')
        else:
            # Print form errors for debugging
            print(form.errors)
            messages.error(request, "There was an error with your registration. Please try again.")
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})



def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in!")
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials. Please try again.")
                return redirect('login')
        else:
            messages.error(request, "Invalid form submission. Please try again.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})




def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')



@login_required
def update_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile', pk=request.user.profile.pk)
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'update_user.html', {'form': form})
