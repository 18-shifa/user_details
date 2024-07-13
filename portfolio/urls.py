from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('portfolio/work_experience/create/', views.work_experience_create, name='work_experience_create'),
    path('portfolio/education/create/', views.education_create, name='education_create'),
    path('portfolio/certification/create/', views.certification_create, name='certification_create'),
    path('work_experience/<int:pk>/edit/', views.work_experience_edit, name='work_experience_edit'),
    path('work_experience/<int:pk>/delete/', views.work_experience_delete, name='work_experience_delete'),
    # Define similar paths for education and certification edit/delete
    path('education/<int:pk>/edit/', views.education_edit, name='education_edit'),
    path('education/<int:pk>/delete/', views.education_delete, name='education_delete'),
    path('certification/<int:pk>/edit/', views.certification_edit, name='certification_edit'),
    path('certification/<int:pk>/delete/', views.certification_delete, name='certification_delete'),

]