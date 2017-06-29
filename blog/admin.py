from django.contrib import admin
from blog.models import UserProfile, Post

admin.site.register(UserProfile)
admin.site.register(Post)