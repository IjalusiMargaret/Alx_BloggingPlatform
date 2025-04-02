from rest_framework import serializers
from .models import Post, Comment, Category, Profile, Like, Subscription
from django.contrib.auth.models import User
from markdownify.templatetags.markdownify import markdownify

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    likes_count = serializers.SerializerMethodField()
    content_html = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'  

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_content_html(self, obj):
        return markdownify(obj.content)

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
