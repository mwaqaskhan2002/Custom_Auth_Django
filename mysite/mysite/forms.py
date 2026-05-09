from django.contrib.auth.forms import PasswordResetForm, AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

class EmailLoginForm(AuthenticationForm): 
    username = forms.EmailField(label="Email or Username", widget=forms.EmailInput(attrs={'class': 'form-control',
        'placeholder': 'Email or Username'})) 
    
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address',
        })
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
        

class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("This Email does not exist in our record.")
        return email
