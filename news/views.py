from django.shortcuts import render
from .models import NewsPost
# Create your views here.

def index(request):
    news = NewsPost.objects.all()
    title = "Главная страница"
    return render(request, 'news/news_feed.html', {"news": news, "title": title})

def news_detail(request, pk):
    news = NewsPost.objects.get(pk=pk)
    title = news.title
    return render(request, 'news/news_detail.html', {"news": news, "title": title})