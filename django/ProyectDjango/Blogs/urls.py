from django.urls import path
from Blogs import views

urlpatterns = [
    path("listTheArticles/", views.getListTheArticles, name="listTheArticles"),
    path("category/<str:categoryId>/", views.category, name="category"),
    path("pageArticle/<str:articleId>/", views.pageArticle, name="pageArticle"),
]
