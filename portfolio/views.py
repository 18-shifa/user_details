from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WorkExperience, Education, Certification
from .forms import WorkExperienceForm, EducationForm, CertificationForm
from django.http import HttpResponseRedirect
from django.urls import reverse



@login_required
def portfolio_view(request):
    work_experiences = WorkExperience.objects.all()
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    return render(request, 'portfolio/portfolio.html', {
        'work_experiences': work_experiences,
        'educations': educations,
        'certifications': certifications
    })

@login_required
def work_experience_create(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = WorkExperienceForm()
    return render(request, 'portfolio/work_experience_form.html', {'form': form})

@login_required
def education_create(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = EducationForm()
    return render(request, 'portfolio/education_form.html', {'form': form})

@login_required
def certification_create(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = CertificationForm()
    return render(request, 'portfolio/certification_form.html', {'form': form})

def work_experience_edit(request, pk):
    instance = get_object_or_404(WorkExperience, pk=pk)
    form = WorkExperienceForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio'))
    return render(request, 'portfolio/work_experience_edit.html', {'form': form})


def work_experience_delete(request, pk):
    experience = get_object_or_404(WorkExperience, pk=pk)
    if request.method == 'POST':
        experience.delete()
        return redirect('portfolio')  # Replace with the appropriate URL name
    # Handle GET request if needed
    return redirect('portfolio')  # Replace with the appropriate URL name



def education_edit(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('portfolio')  # Replace with the appropriate URL name
    else:
        form = EducationForm(instance=education)
    
    return render(request, 'portfolio/education_edit.html', {'form': form})


def education_delete(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        education.delete()
        return redirect('portfolio')  # Replace with the appropriate URL name
    # Handle GET request if needed, perhaps show a confirmation form
    return redirect('portfolio')  # Replace with the appropriate URL name



def certification_edit(request, pk):
    certification = get_object_or_404(Certification, pk=pk)
    if request.method == 'POST':
        form = CertificationForm(request.POST, instance=certification)
        if form.is_valid():
            form.save()
            return redirect('portfolio')  # Replace with the appropriate URL name
    else:
        form = CertificationForm(instance=certification)
    return render(request, 'portfolio/certification_edit.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from .models import Certification

def certification_delete(request, pk):
    certification = get_object_or_404(Certification, pk=pk)
    if request.method == 'POST':
        certification.delete()
        return redirect('portfolio')  # Replace with the appropriate URL name
    return render(request, 'certification_delete.html', {'certification': certification})
