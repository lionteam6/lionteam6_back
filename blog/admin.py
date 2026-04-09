from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price', 'max_participants')
    filter_horizontal = ('participants',)

# Register your models here.
