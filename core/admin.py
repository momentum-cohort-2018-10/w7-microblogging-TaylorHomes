from django.contrib import admin
from core.models import Post, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ("user", "title", "body")


admin.site.register(Post, PostAdmin)
admin.site.register(User)