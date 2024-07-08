from django.urls import path
from .views import IndexView, ContactView, View404, View500
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', IndexView.as_view(), name='index'), #htopprojetos
    # path('projetos/', IndexView.as_view(), name='projects'),
    path('contato/', ContactView.as_view(), name='contact'),
]

handler404 = View404.as_view()
handler500 = View500.as_view()