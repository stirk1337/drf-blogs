from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# class BlogAPIUpdate(generics.UpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#
# class BlogAPIView(generics.ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#
# class BlogAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


