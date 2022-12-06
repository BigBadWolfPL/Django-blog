from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),                         # views.home
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.to_samo_co_posts_list_view, name='blog-about'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('test/', views.TestTemplateView.as_view(), name='test'),
    path('search/', views.search, name='search')

]