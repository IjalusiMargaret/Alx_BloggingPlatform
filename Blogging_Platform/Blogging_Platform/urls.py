from django.contrib import admin
from django.urls import path, include
from Blog.views import welcome_view  # Ensure you have a welcome view

urlpatterns = [
    path("", welcome_view, name="welcome"),  # Set welcome_view as root
    path("admin/", admin.site.urls),
    path("Blog/", include("Blog.urls")),  # Adjust as per your app name
]
