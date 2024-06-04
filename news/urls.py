from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path('', views.index, name="index"),
    path("detail/<int:pk>/", views.news_detail, name="news_detail"),
    path("create/", views.create_post, name="create_post"),
    path("update/<int:pk>/", views.update_post, name="update_post"),
    #path("delete/<int:pk>/", views.news_delete, name="news_delete"),
    #path("comment/<int:pk>/", views.add_comment_to_news, name="add_comment_to_news"),
]