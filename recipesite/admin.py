from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'cuisine', 'created_on')
    search_fields = ['cuisine', 'title', 'author']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('cuisine', 'created_on',)
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body')
    list_filter = ('approved', 'created_on')
    search_fields = ('email', 'post')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    