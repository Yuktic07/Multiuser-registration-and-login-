from django.shortcuts import render, redirect
from django.urls import reverse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import UserRegistrationForm, UserProfileForm, UserLoginForm
from .models import UserProfile 
from django.views import View 



class RegisterView(TemplateView):
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
        login_form = UserLoginForm()
        return self.render_to_response({'user_form': user_form, 'profile_form': profile_form, 'login_form': login_form})

    def post(self, request, *args, **kwargs):
        user_form = UserRegistrationForm(request.POST, request.FILES)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            password = user_form.cleaned_data['password']
            confirm_password = user_form.cleaned_data['confirm_password']

            if password == confirm_password:
                user = user_form.save()
                user.set_password(password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                login(request, user)

                if profile.is_doctor:
                    return redirect('doctor_dashboard')
                else:
                    # Redirect to the login page after successful registration
                    return redirect(reverse('login'))

            else:
                user_form.add_error('confirm_password', 'Passwords do not match')

        login_form = UserLoginForm()
        return self.render_to_response({'user_form': user_form, 'profile_form': profile_form, 'login_form': login_form})


class LoginView(View):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        login_form = UserLoginForm()
        return render(request, self.template_name, {'login_form': login_form})

    def post(self, request, *args, **kwargs):
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                profile = UserProfile.objects.get(user=user)
                if profile.is_doctor:
                    return redirect('doctor_dashboard')
                else:
                    return redirect('patient_dashboard')

        return render(request, self.template_name, {'login_form': login_form})

@login_required
def doctor_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'dashboard/doctor_dashboard.html',context)

@login_required
def patient_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'dashboard/patient_dashboard.html',context)

def custom_logout(request):
    logout(request)
    return redirect('login')