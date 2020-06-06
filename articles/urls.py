from django.urls import path
from articles.views import (
    list_article_page,
    submit_article_page,
    detail_article_page,
    submit_comment,
    list_askme_page,
    submit_askme_page,
    detail_askme_page,
    delete_askme_page,
    edit_askme_page,
    statistic_page
)

app_name = 'articles'

urlpatterns = [
    path('list/', list_article_page, name='list'),
    path('submit/', submit_article_page, name='submit'),
    path('detail/<int:article_id>', detail_article_page, name='detail'),
    path('comment/<int:article_id>', submit_comment, name='comment'),
    path('askme/', list_askme_page, name='list_askme'),
    path('askme/submit/', submit_askme_page, name='submit_askme'),
    path('askme/detail/<int:askme_id>', detail_askme_page, name='detail_askme'),
    path('delete/<int:askme_id>', delete_askme_page, name='delete_askme'),
    path('edit/<int:askme_id>', edit_askme_page, name='edit_askme'),
    path('statistic/', statistic_page, name='statistic'),
]