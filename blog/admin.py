from django.contrib import admin
from .models import Blog, Category, Author

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Category)
