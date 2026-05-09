from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, LoginView
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm, EmailLoginForm, SignUpForm 
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin



class MyLoginView(LoginView):
    form_class = EmailLoginForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    success_message = ("Account created successfully. You can now log in.")
    
    # def get(self, request):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})
    
    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(self.success_url)
    #     return render(request, self.template_name, {'form': form})        

class MyPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm  
    template_name = 'registration/password_reset_form.html'
    html_email_template_name = 'registration/emails/password_reset_email.html'  # ✅ HTML email
    subject_template_name = 'registration/emails/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    from_email = 'My Site <noreply@myapp.com>'  
        
    
class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        if not context.get('validlink'):
            print("Your Token is expired or invalid. Please request a new password reset.")
        return context
    

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = 'login'  # Redirect to login page if not authenticated
