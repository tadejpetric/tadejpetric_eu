from django.urls import include, path
from . import views

urlpatterns = [
    #path('', views.login, name='login_racuni'),
    path('login', views.login, name='login_racuni'),
    path('form_input_anonymous', views.form_input_anonymous,
         name="form_input_anonymous_racuni"),
    path('result', views.result, name='result_racuni'),
    path('homepage', views.homepage, name='homepage_racuni'),
    path('form_input', views.form_input, name='form_input_racuni'),
    path('settings', views.settings, name='settings_racuni'),
]
