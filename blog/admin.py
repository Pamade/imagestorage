from django.contrib import admin
from .models import Post
from users.models import Media


admin.site.register(Post)
admin.site.register(Media)
