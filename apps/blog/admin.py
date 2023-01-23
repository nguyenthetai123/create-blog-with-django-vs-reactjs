from django.contrib import admin

# Register your models here.
from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
