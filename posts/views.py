from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
from .models import Topic, Category, Post


def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)


def topic_list(request):
    # pobieramy wszystkie obiekty Topic z bazy poprzez QuerySet
    topics = Topic.objects.all()
    return render(request,
                  "posts/topic/list.html",
                  {'topics': topics})


def topic_detail(request, id):
    # pobieramy konkretny obiekt Topic
    try:
        topic = Topic.objects.get(id=id)
    except Topic.DoesNotExist:
        raise Http404("Obiekt Topic o podanym id nie istnieje")

    return render(request,
                  "posts/topic/detail.html",
                  {'topic': topic})


def category_list(request):
    # pobieramy wszystkie obiekty Category z bazy poprzez QuerySet
    categories = Category.objects.all()

    return render(request,
                  "posts/category/list.html",
                  {'categories': categories})


def category_detail(request, id):
    # pobieramy konkretny obiekt Category
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404("Obiekt Category o podanym id nie istnieje")

    return render(request,
                  "posts/category/detail.html",
                  {'category': category})


def post_list(request):
    # pobieramy wszystkie obiekty Post z bazy poprzez QuerySet
    posts = Post.objects.all()
    return render(request,
                  "posts/post/list.html",
                  {'posts': posts})


def post_detail(request, id):
    # pobieramy konkretny obiekt Post
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Obiekt Post o podanym id nie istnieje")

    return render(request,
                  "posts/post/detail.html",
                  {'post': post})


def topic_posts(request, id):
    # pobieramy konkretny obiekt Topic
    try:
        topic = Topic.objects.get(id=id)
    except Topic.DoesNotExist:
        raise Http404("Obiekt Topic o podanym id nie istnieje")

    # pobieramy wszystkie posty dla danego topiku, sortowane od najnowszych
    posts = Post.objects.filter(topic=topic).order_by('-created_at')

    return render(request,
                  "posts/topic/posts.html",
                  {'topic': topic, 'posts': posts})
