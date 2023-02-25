from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class CommentInline(admin.TabularInline): # StackedInline
    model = Comment
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
