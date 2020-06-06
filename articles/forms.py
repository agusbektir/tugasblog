from django import forms
from articles.models import Article, Comment, AskMe


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'slug', 'category']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

class AskMeForm(forms.ModelForm):

    class Meta:
        model = AskMe
        fields = ['title', 'question', 'category']