from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from blog.views import *

router = routers.SimpleRouter()
router.register(r'blog', BlogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
