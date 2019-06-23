from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index_racuni'),
    path('result', views.result, name='result_racuni'),
    path('form_input', views.form_input, name='form_input_racuni')
]
