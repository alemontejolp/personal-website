from django.urls import path
from . import views

urlpatterns = [
  path('', views.about_me, name='apps.aboutme.me'),
  path('projects/', views.projects, name='apps.aboutme.projects'),
  path('projects/<int:project_id>', views.project_details, name='apps.aboutme.project_details')
]
