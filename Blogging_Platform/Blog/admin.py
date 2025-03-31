from django.contrib import admin
from .models import Post, Category, Comment
from .models import  Like
from .models import Subscription, Profile  # Ensure Subscribe model is imported

admin.site.register(Subscription) 
admin.site.register(Profile)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    search_fields = ('user__username', 'post__title')
    list_filter = ('created_at',)

admin.site.register(Like, LikeAdmin)


@admin.register(Post)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_date', 'created_at')
    list_filter = ('category', 'published_date', 'tags')
    search_fields = ('title', 'content', 'author__username', 'tags__name')
    prepopulated_fields = {'slug': ('title',)}  # if you add a slug field later


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    search_fields = ('user__username', 'post__title', 'content')
