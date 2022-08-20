from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('english/', views.english, name='english'),
        path('englishmemes/', views.englishmemes, name='englishmemes'),
    path('base/', views.base, name='base'),
]