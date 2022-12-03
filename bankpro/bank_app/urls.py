from django.urls import path
from . import views
app_name = 'bank_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('application',views.apply,name='apply'),
    path('control',views.control,name='ctrl'),
    path('about',views.about,name='about'),
]