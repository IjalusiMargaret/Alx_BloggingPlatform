'''from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
#from django.urls import path
from .views import welcome_view


urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('posts/<int:post_id>/share/', share_post, name='post-share'),

    #path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='post-comments'),

    path('posts/<int:post_id>/like/', views.LikeView.as_view(), name='post-like'),
    path('subscribe/', views.SubscriptionView.as_view(), name='subscribe'),
]
'''



from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),  # Root welcome view
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('posts/<int:post_id>/share/', views.share_post, name='post-share'),
    path('posts/<int:post_id>/like/', views.LikeView.as_view(), name='post-like'),
    path('subscribe/', views.SubscriptionView.as_view(), name='subscribe'),
]
