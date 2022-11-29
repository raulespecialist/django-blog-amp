from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Page, PageImage, Post, PostImage

class PageImageAdmin(admin.StackedInline):
    model = PageImage

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug','created_date')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('text',)
    inlines = [PageImageAdmin]

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug','created_date')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('text',)
    inlines = [PostImageAdmin]


#admin.site.register(Page)
#admin.site.register(Post)