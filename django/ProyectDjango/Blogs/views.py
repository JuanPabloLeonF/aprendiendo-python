from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from Blogs import models

@login_required(login_url="logingPage")
def getListTheArticles(request):
    listArticles = models.Article.objects.order_by('createDate')
    paginator = Paginator(listArticles, 6)
    page = request.GET.get("page")
    
    try:
        pageArticle = paginator.page(page)
    except PageNotAnInteger:
        pageArticle = paginator.page(1)
    except EmptyPage:
        pageArticle = paginator.page(paginator.num_pages)
    
    context = {
        "title": "Articulos",
        "listArticles": pageArticle
    }
    return render(request, "articles/listTheArticles.html", context)

@login_required(login_url="logingPage")
def category(request, categoryId):
    category = models.Category.objects.get(id=categoryId)
    listArticles = models.Article.objects.filter(categories=category)
    
    context = {
        "category": category,
        "listArticles": listArticles
    }
    return render(request, "categories/category.html", context)

@login_required(login_url="logingPage")
def pageArticle(request, articleId):
    article = models.Article.objects.get(id=articleId)
    context = {
        "article": article
    }
    return render(request, "articles/pageArticle.html", context)
    