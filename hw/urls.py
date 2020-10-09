from django.urls import path
from hw.views import index, article, articles, archive_article, articles_archive, user, users

urlpatterns = [
    path('', index, name='index'),
    path('article/<int:article_id>/', article, name='article'),
    path('articles/<int:article_id>/archive/', archive_article, name='archive_article'),
    path('user/<int:user_id>/', user, name='user'),
    path('articles/', articles, name='articles'),
    path('articles/archive/', articles_archive, name='articles_archive'),
    path('users/', users, name='users'),
]