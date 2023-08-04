from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from blog.views import *

# router = routers.SimpleRouter()
# router.register(r'blog', BlogViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls')),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/blog/', BlogAPIList.as_view()),
    path('api/v1/blog/<int:pk>/', BlogAPIUpdate.as_view()),
    path('api/v1/blogdelete/<int:pk>/', BlogAPIDestroy.as_view()),
]