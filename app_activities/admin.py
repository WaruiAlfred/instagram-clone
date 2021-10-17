from django.contrib import admin
from .models import Image,Follow,Comment,Like

admin.site.register(Image)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Like)