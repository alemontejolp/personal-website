import markdown
from django.shortcuts import render, get_object_or_404
from apps.main.utils.global_menu import MENU_STATE_PROP, MenuState
from apps.main.utils import global_menu
from . import models

# Create your views here.
def about_me(request):
  projects = models.Project.objects.filter(show_in_landing__exact = True).order_by('-id')
  jobs = models.Job.objects.all().order_by('-id')
  for j in jobs:
    j.description = markdown.markdown(j.description)
  return render(request, 'aboutme/about_me.html', {
    'projects': projects,
    'jobs': jobs,
    MENU_STATE_PROP: MenuState(global_menu.MENU_ITEM_ABOUT_ME)
  })


def projects(request):
  projects = models.Project.objects.filter(show_in_landing__exact = True).order_by('-id')
  return render(request, 'aboutme/projects.html', {
    'projects': projects,
    MENU_STATE_PROP: MenuState(global_menu.MENU_ITEM_PROJECTS)
  })


def project_details(request, project_id):
  # project = models.Project.objects.get(id = project_id)
  project = get_object_or_404(models.Project, id = project_id)
  project.content = markdown.markdown(project.content)
  return render(request, 'aboutme/project_details.html', {
    'project': project
  })
