from django.contrib import admin
from .models import Post, Category

admin.site.register(Post)  # admin 페이지에 블로그 Post 작성이 가능해짐

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Category, CategoryAdmin)