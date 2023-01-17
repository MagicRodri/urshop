
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()

class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = '__all__'


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class PpUploadForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['picture'].widget = forms.FileInput(
            attrs={'class':'form-control-file','value':''},
            )
            
    class Meta:
        model = User
        fields = ['picture']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
