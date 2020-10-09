from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("index")


def articles(request):
    return HttpResponse('There will be a list with articles')


def articles_archive(request):
    return HttpResponse('There will be a list with archived articles')


def users(request):
    return HttpResponse('There will be a list with users')


def article(request, article_id):
    return HttpResponse(f"This is an article #{article_id}")


def archive_article(request, article_id):
    return HttpResponse(f"This is an archived article #{article_id}")


def user(request, user_id):
    return HttpResponse(f"This is an user #{user_id}")
