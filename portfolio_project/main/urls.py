from django.urls import path
from main import views

urlpatterns = [
    path('', views.base, name='base'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
]