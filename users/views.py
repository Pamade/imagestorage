from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, Http404
from django.contrib.auth import update_session_auth_hash
from .forms import UserRegisterForm, MediaForm, SettingsForm
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import Media
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})




@login_required
def add_media(request):
    
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user= request.user        
            form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = MediaForm()

    return render(request, 'users/add_media.html', {'form':form})

@login_required
def profile(request):
    
    if request.method == 'GET':        
        media_images = Media.objects.filter(user=request.user)
         
    context = {
        'media_images':media_images,  
        
    }
    return render(request, 'users/profile.html', context)


def edit_post(request, pk):
    template = 'users/add_media.html'
    post = get_object_or_404(Media, pk=pk)
    if post.user == request.user:
        if request.method == 'POST':
            
            form = MediaForm(request.POST, instance=post)
            try:
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Media updated')
            except Exception as e:
                messages.warning(request, 'Your post not saved {}'.format(e))
                
        else:
            form = MediaForm(instance = post)
    else:
        raise Http404
    context = {
        'form':form,
        'post':post
    }
    return render(request, template, context)
def delete_view(request, media_id = None):
    delete_object = Media.objects.get(id=media_id)
    delete_object.delete()
    return redirect('http://127.0.0.1:8000/profile/')

def change_username(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Profile updated')
            return redirect('profile')
    else:
        form = SettingsForm()

    return render(request, 'users/change_username.html', {'form':form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user) 

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    
    return render(request, 'users/change_password.html', {'form':form})

# def change_profile_image(request):
