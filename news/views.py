from django.shortcuts import render, redirect
from .models import NewsPost, Comment
from .forms import PostModelForm, CommentModelForm
from datetime import datetime
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    news = NewsPost.objects.all()
    search = request.GET.get("search")

    if search:
        news = news.filter(title__icontains=search)

    paginator = Paginator(news, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)    

    title = "Главная страница"
    return render(request, 'news/news_feed.html', {"page_obj": page_obj, "title": title})

def news_detail(request, pk):
    news = NewsPost.objects.all()
    post = news.get(pk=pk)
    title = post.title

    count = str(request.GET.get("post"))
    comments = Comment.objects.filter(post=post).order_by("-date_published")

    if count == "prev":
        if post.id == news.first().id:
            return redirect("news:news_detail", pk=news.last().id)
        prev_post = news.filter(id__lt=post.id).last()
        return redirect("news:news_detail", prev_post.id)
    
    if count == "next":
        if post.id == news.last().id:
            return redirect("news:news_detail", pk=news.first().id)
        next_post = news.filter(id__gt=post.id).first()
        return redirect("news:news_detail", next_post.id)
    
    context = {
        "post": post,
        "title": title,
        "comments": comments,
    }

    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.date_published = datetime.now()
            new_comment.post = post
            new_comment.save()
            return redirect("news:news_detail", pk=pk)
    else:
        form = CommentModelForm()

    context["form"] = form

    return render(request, 'news/news_detail.html', context)

def create_post(request):
    title = "Создание поста"
    action = "Создать"
    form = PostModelForm()

    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.date_published = datetime.now()
            new_post.save()
            return redirect("news:index")
        else:
            form = PostModelForm()

    return render(request, 'news/create_update_post.html', {"title": title, "form": form, "action": action})

def update_post(request, pk):
    action = "Изменить"
    news = NewsPost.objects.all()
    post = news.get(pk=pk)
    title = f"Изменение {post.title}"
    form = PostModelForm(instance=post)

    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("news:news_detail", pk=pk)
        else:
            form = PostModelForm(instance=post)

    return render(request, 'news/create_update_post.html', {"title": title, "form": form, "action": action})