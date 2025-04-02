from rest_framework import generics, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Post, Comment, Category, Like, Subscription
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, LikeSerializer, SubscriptionSerializer

def welcome_view(request):
    return JsonResponse({
        "message": """
        Welcome to my Blogging Platform, a dynamic content management system designed for both bloggers and readers. Built with Django REST Framework, this platform offers a user-friendly and scalable solution for creating, managing, and interacting with blog content.

        Key Features:

        1. User Authentication and Profile Management
        Secure user registration, login, and profile management, allowing users to personalize their profiles with bio and profile pictures.

        2. Post Creation and Management
        Bloggers can create, edit, and manage posts, categorize them, and assign tags for better discoverability.

        3. Categories and Tags
        Content is organized into categories, with posts tagged by keywords for easy searching and exploration.

        4. Commenting and Liking
        Users can comment on posts and like them, with full CRUD functionality for comments and a unique like system to ensure a user can like a post only once.

        5. Subscriptions
        Users can subscribe to other bloggers or categories to stay updated on new posts and content.

        6. Post Sharing
        Posts can be shared via email, helping to extend their reach beyond the platform.

        7. Search and Filter
        Advanced search and filter features enable users to easily find posts by category, tag, and keywords.

        8. Full-Featured REST API
        The platform offers a fully integrated API, supporting post creation, commenting, liking, subscriptions, and more, enabling third-party integrations.
        """
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def share_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    recipient_email = request.data.get('email')
    post_link = f"http://yourdomain.com/posts/{post.id}/"
    
    send_mail(
        subject=f"Check out this post: {post.title}",
        message=f"Read the post here: {post_link}",
        from_email="noreply@blog.com",
        recipient_list=[recipient_email],
    )
    return Response({"message": "Post shared successfully!"})

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'tags__name', 'author__username']
    ordering_fields = ['published_date', 'category__name']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        
        instance = self.get_object()
    
        self.perform_destroy(instance)
        
        return Response({"message": "This post has been deleted"}, status=status.HTTP_204_NO_CONTENT)


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post__id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(user=self.request.user, post=post)


class LikeView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubscriptionView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]




class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class UnlikeView(generics.DestroyAPIView):
    serializer_class = LikeSerializer

    def get_object(self):
        
        user = self.request.user
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return get_object_or_404(Like, user=user, post=post)

    def delete(self, request, *args, **kwargs):
        
        self.perform_destroy(self.get_object())
        return Response({"detail": "You have unliked this post."}, status=status.HTTP_204_NO_CONTENT)
