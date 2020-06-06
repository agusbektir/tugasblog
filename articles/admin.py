from django.contrib import admin
from articles.models import Article, Category, Comment, QuestionCategory, AskMe


class CategoryAdminPage(admin.ModelAdmin):
    list_display = ['name']

class ArticleAdminPage(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'category', 'is_published']
    list_filter = ['is_published']
    search_fields = ['title']

class CommentAdminPage(admin.ModelAdmin):
    list_filter = ['article', 'content']

class QuestionCategoryAdminPage(admin.ModelAdmin):
    list_display = ['name']

class AskMeAdminPage(admin.ModelAdmin):
    list_display = ['category', 'title', 'author']
    list_filter = ['category']

admin.site.register(Category, CategoryAdminPage)
admin.site.register(Article, ArticleAdminPage)
admin.site.register(Comment, CommentAdminPage)
admin.site.register(QuestionCategory, QuestionCategoryAdminPage)
admin.site.register(AskMe, AskMeAdminPage)