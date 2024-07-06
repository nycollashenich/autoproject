from django.urls import path
from .views import IndexView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index'), #htopprojetos
    # path('projetos/', IndexView.as_view(), name='projects'),
    path('contato/', ContactView.as_view(), name='contact'),
]