from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analiza/', include('page.analiza.urls')),
    path('racuni/', include('page.racuni.urls')),
]
