from django.urls import path
from .views import IndexView, ContactView, View404, View500, ProjectDetailView, ProjectListView
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', IndexView.as_view(), name='index'), #htopprojetos
    path('contato/', ContactView.as_view(), name='contact'),
    path('project/<slug:slug>', ProjectDetailView.as_view(), name='project'),
    path('projectlist/', ProjectListView.as_view(), name='projectlist')

]

handler404 = View404.as_view()
handler500 = View500.as_view()