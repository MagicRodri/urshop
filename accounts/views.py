
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from carts.models import Cart

from .forms import EditProfileForm, LoginForm, PpUploadForm, SignUpForm

# Create your views here.

User = get_user_model()

def login_view(request):

    form = LoginForm(request)
    message = ""
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            
            # Grab the session cart and assign it to the user
            cart, created = Cart.objects.get_or_new(request)
            if not created:
                cart.cart_id = ''
            cart.user = user
            cart.save()
            # set user backend to the default to avoid multiple authentication backends conflict
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,user)
            return redirect(reverse('home'))

        else:
            message = "Login failed"
            
    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'accounts/login.html',context = context)


def logout_view(request):

    if request.method == 'POST':
        logout(request)
        return redirect(reverse('accounts:login'))

    return render(request,'accounts/logout.html',context={})


def signup_view(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user=form.save()
            # set user backend to the default to avoid multiple authentication backends conflict
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,user)
            return redirect(reverse('home'))

    return render(request,'accounts/signup.html',context={'form':form})


def upload_pp_view(request):
    form = PpUploadForm(instance=request.user)
    if request.method == 'POST':
        form = PpUploadForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    context = {
        'form' : form
    }
    return render(request,'accounts/upload_profile_picture.html',context=context)

def edit_profile_view(request):
    user = request.user
    form = EditProfileForm(instance=user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    context = {
        'form' : form
    }

    return render(request,'accounts/edit_profile.html',context=context)

def delete_profile_view(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        return redirect(reverse('accounts:login'))

    return render(request,'accounts/delete_profile.html',context={})