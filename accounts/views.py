
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import UpdateView

from carts.models import Cart

from .forms import EditProfileForm, LoginForm, PpUploadForm, SignUpForm

User = get_user_model()

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('home')
    
    def form_valid(self, form):
        # Grab the session cart and assign it to the user
        guess_cart, _ = Cart.objects.get_or_new(self.request)
        user = form.get_user()
        # set user backend to the default to avoid multiple
        # authentication backends conflict
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request,user)
        user_cart, _ = Cart.objects.get_or_new(self.request)
        for item in guess_cart.items.all():
            item.cart = user_cart
            item.save()
        
        guess_cart.delete()
        return super().form_valid(form)

class UploadPpView(UpdateView):
    model = User
    form_class = PpUploadForm
    template_name = 'accounts/upload_profile_picture.html'

    def get_success_url(self):
        return reverse('home')

    def get_object(self):
        return self.request.user


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(reverse('accounts:login'))
    return render(request,'accounts/logout.html')


def signup_view(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            # set user backend to the default to avoid multiple authentication backends conflict
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,user)
            return redirect(reverse('accounts:upload-pp'))

    return render(request,'accounts/signup.html',context={'form':form})

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