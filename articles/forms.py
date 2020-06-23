from django import forms
from articles.models import Article, Comment, AskMe


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'slug', 'category', 'image']

# class ArticlePhotoForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ['image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class AskMeForm(forms.ModelForm):
    class Meta:
        model = AskMe
        fields = ['title', 'question', 'category']