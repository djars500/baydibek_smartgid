from django.shortcuts import render, get_object_or_404
from .models import *

def main(request):

    news = News.objects.all()[:2]

    context = {
        'news': news
    }
    return render(request, 'index.html', context)

def historyBaidybekView(request):
    return render(request, 'historyBaidybek.html')

def shayanView(request):
    return render(request, 'shayan.html')

def borlisayView(request):
    return render(request, 'borlisay.html')

def category_detailView(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Posts.objects.filter(category=category)

    data = {
        'category': category,
        'posts': posts
    }

    return render(request, 'category.html', data)


def mediaCategory_detailView(request, slug):
    category = MediaCategory.objects.get(slug=slug)
    posts = PostMedia.objects.filter(media_category=category)

    data = {
        'category': category,
        'posts': posts
    }

    return render(request, 'category.html', data)

def postDetailView(request, slug):
    post = Posts.objects.get(slug=slug)
    category = post.category
    category_url = reverse('category_detailView', args=[category.slug])
    data = {
        'post': post,
        'category_url': category_url
    }



    return render(request, 'single-page.html', data)

def mediaPostDetailView(request, slug):
    post= PostMedia.objects.get(slug=slug)
    category = post.media_category
    category_url = reverse('mediaCategory_detailView', args=[category.slug])
    data = {
        'post': post,
        'category_url': category_url
    }

    return render(request, 'single-page.html', data)