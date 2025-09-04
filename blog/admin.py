from django.contrib import admin
from blog.models import Post, Category, Comment
from django_mptt_admin.admin import DjangoMpttAdmin


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ-панель модели категорий
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Админ-панель модели записей
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdminPage(DjangoMpttAdmin):
    """Админ-панель модели комментариев"""
    pass
