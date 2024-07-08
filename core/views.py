from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView
from .models import Project

class IndexView(TemplateView):
    template_name = 'index.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects_detail.html'
    context_object_name = 'project'
    slug_field = 'slug'

class ProjectListView(ListView):
    model = Project
    template_name = 'projects_list.html'
    context_object_name = 'projects'

# page error
from django.views import View
class View404(View): 
    def get(self, request, *args, **kwargs):
        return render(request, '404.html', status=404)

class View500(View):
    def get(self, request, *args, **kwargs):
        return render(request, '500.html', status=500)