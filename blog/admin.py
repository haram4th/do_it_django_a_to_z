from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Tag

 
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Post, MarkdownxModelAdmin) # admin 페이지에 블로그 Post 작성이 가능해짐
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)