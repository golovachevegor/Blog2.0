from django.contrib import admin
from blog.models import Post, Category
from django_mptt_admin.admin import DjangoMpttAdmin


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ-панель модели категорий
    """
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post)
