from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'), # views.home
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/<int:pk>', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('testowy/', views.testowy, name='blog-testowy'),
]