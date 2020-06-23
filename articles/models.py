import os
from django.db import models

from helpers.models import BaseModel
from members.models import Member


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

def image_article_path(instance, filename):
    return os.path.join('article_pic', instance.title, filename)


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.SlugField()
    published_at = models.DateTimeField(null=True)
    is_published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to=image_article_path, default='')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(Member, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.article.title}: {self.content}'

class QuestionCategory(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AskMe(BaseModel):
    title = models.CharField(max_length=200)
    question = models.TextField()
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category.name}: {self.question}'