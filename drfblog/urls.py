from django.contrib import admin
from django.urls import path

from blog.views import BlogAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/bloglist', BlogAPIView.as_view()),
]
