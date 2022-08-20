from django.urls import path 
from . import views


urlpatterns = [
    
    path('malayalam', views.malayalam, name='malayalam'),
    path('official/', views.official, name='official')
    
]