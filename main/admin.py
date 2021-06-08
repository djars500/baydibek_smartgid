from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class MediaCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class PostCategoryAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    prepopulated_fields = {"slug": ("title",)}

class PostMediaCategoryAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    prepopulated_fields = {"slug": ("title",)}

class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(MediaCategory, MediaCategoryAdmin)
admin.site.register(Posts, PostCategoryAdmin)
admin.site.register(PostMedia, PostMediaCategoryAdmin)
admin.site.register(News, NewsAdmin)