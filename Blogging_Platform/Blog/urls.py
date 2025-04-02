from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),  # Root welcome view
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('posts/<int:post_id>/share/', views.share_post, name='post-share'),
    path('posts/<int:post_id>/like/', views.LikeView.as_view(), name='post-like'),
    path('subscribe/', views.SubscriptionView.as_view(), name='subscribe'),
    path('posts/<int:post_id>/unlike/', views.UnlikeView.as_view(), name='post-unlike'),
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('posts/<int:post_id>/share/', views.share_post, name='share_post'),
]
