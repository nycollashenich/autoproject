from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView, FormView
from .models import Project
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(TemplateView):
    template_name = 'index.html'

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(ContactView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar mensagem')
        return super(ContactView, self).form_invalid(form, *args, **kwargs)
    
    
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