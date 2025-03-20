from rest_framework import generics, permissions, filters
from .models import Post, Comment, Category, Like, Subscription
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, LikeSerializer, SubscriptionSerializer

from django.core.mail import send_mail

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def share_post(request, post_id):
    post = Post.objects.get(id=post_id)
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

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post__id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

class LikeView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubscriptionView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
