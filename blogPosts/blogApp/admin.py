from django.contrib import admin

from blogApp.models import UserInfo, BlogPost, PostComment

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(BlogPost)
admin.site.register(PostComment)