from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from articles.forms import ArticleForm, CommentForm, AskMeForm
from articles.models import Article, Comment, AskMe
from members.models import Member


def list_article_page(request):
    articles = Article.objects.all()
    most_commented_articles = (Article.objects.annotate(total_comment=Count('comment'))
                               .order_by('-total_comment')[:1])
    most_commenter = (Member.objects.annotate(total_comment=Count('comment'))
                          .order_by('-total_comment')[:1])
    context = {
        'articles':articles,
        'most_commented_articles': most_commented_articles,
        'most_commenter': most_commenter
    }
    return render(request, 'articles/list.html', context)

def submit_article_page(request):
    form = ArticleForm(request.POST or None, use_required_attribute=False)
    if form.is_valid():
        form.save()
        return redirect('articles:list')
    context = {
        'form':form
    }
    return render(request, 'articles/submit.html', context)

def detail_article_page(request, article_id):
    form = CommentForm()
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article=article_id)
    context = {
        'form':form,
        'article':article,
        'comments':comments
    }
    return render(request, 'articles/detail.html', context)

@login_required(login_url='members:login')
def submit_comment(request, article_id):
    url = reverse('articles:detail', args=[article_id])
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            article = get_object_or_404(Article, id=article_id)
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user.member
            comment.save()
            return redirect(url)
    return redirect(url)

def list_askme_page(request):
    questions = AskMe.objects.all()
    context = {
        'questions':questions,
    }
    return render(request, 'articles/list_askme.html', context)

def submit_askme_page(request):
    form = AskMeForm(request.POST or None, use_required_attribute=False)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user.member
                question.save()
                url = reverse('articles:list_askme')
                return redirect(url)
    context = {
        'form':form
    }
    if not request.user.is_authenticated:
        if request.method == 'POST':
            url = reverse('members:login')
            return redirect(url)
    return render(request, 'articles/submit_askme.html', context)

def detail_askme_page(request, askme_id):
    question = get_object_or_404(AskMe, id=askme_id)
    context = {
        'question':question
    }
    return render(request, 'articles/detail_askme.html', context)

def delete_askme_page(request, askme_id):
    question = get_object_or_404(AskMe, id=askme_id)
    question.delete()
    return redirect('members:dashboard')

def edit_askme_page(request, askme_id):
    question = get_object_or_404(AskMe, id=askme_id)
    form = AskMeForm(request.POST or None, use_required_attribute=False, instance=question)
    if form.is_valid():
        form.save()
        return redirect('members:dashboard')
    context = {
        'form': form,
    }
    return render(request, 'articles/submit_askme.html', context)

# def statistic_page(request):
#     most_commented_articles = (Article.objects.annotate(total_comment=Count('comment'))
#                                .order_by('-total_comment'))
#     most_commenter = (Member.objects.annotate(total_comment=Count('comment'))
#                           .order_by('-total_comment'))
#     context = {
#         'most_commented_articles': most_commented_articles,
#         'most_commenter':most_commenter
#     }
#     return render(request, 'articles/statistic.html', context)