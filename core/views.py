from django.shortcuts import render

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class ContactView(TemplateView):
    template_name = 'contact.html'




# page error
from django.views import View
class View404(View): 
    def get(self, request, *args, **kwargs):
        return render(request, '404.html', status=404)

class View500(View):
    def get(self, request, *args, **kwargs):
        return render(request, '500.html', status=500)