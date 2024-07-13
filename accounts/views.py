from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from profiles.models import UserProfile
from projects.models import Project
from portfolio.models import WorkExperience, Education, Certification
from .forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')  # Redirect to profile after signup
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Redirect to profile after login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def dashboard_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    projects = Project.objects.all()
    work_experiences = WorkExperience.objects.all()
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    
    context = {
        'projects': projects,
        'work_experiences': work_experiences,
        'educations': educations,
        'certifications': certifications,
        'user_profile': user_profile,
    }
    return render(request, 'dashboard.html', context)
