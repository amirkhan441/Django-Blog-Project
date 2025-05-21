# Register models with the admin site

from django.contrib import admin
from .models import Post

admin.site.register(Post)