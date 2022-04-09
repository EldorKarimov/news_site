from django.shortcuts import render
from .models import Category, City, News

def category_list(request):
    categories = Category.objects.all()
    return {"categories":categories}

def city_list(request):
    cities = City.objects.all()
    return {"cities":cities}

def home(request):
    news = News.objects.all().order_by('-created')

    context = {
        'news':news
    }

    return render(request, 'home.html', context)

def category_news(request, slug):
    category = Category.objects.get(slug=slug)
    new = News.objects.filter(category=category)


    context = {
        'category':category,
        'news':new
    }

    return render(request, 'category_news.html', context)

def city_news(request, slug):
    city = City.objects.get(slug=slug)
    new = News.objects.filter(city=city)

    context = {
        'city': city,
        'news': new
    }

    return render(request, 'city_news.html', context)

def detail_news(request, slug):
    news = News.objects.get(slug=slug)
    last_news = News.objects.all().order_by('-created')
    category_detail_news = News.objects.filter(category = news.category)
    news.views += 1
    news.save()

    context = {
        'news':news,
        'last_news':last_news,
        'category_detail_news':category_detail_news
    }

    return render(request, 'detail_news.html', context)