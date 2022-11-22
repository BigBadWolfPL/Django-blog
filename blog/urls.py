from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('moja/', views.moja, name='blog-moja'),
    path('kontakt/', views.kontakt, name='blog-kontakt'),
]