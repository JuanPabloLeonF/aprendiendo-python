from django.shortcuts import render, redirect
from myApp import models, forms
from django.contrib import messages

def index(request):
    articles = models.Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, "index.html", context)

def helloWord(request):
    return render(request, "helloWord.html")
    
def contact(request, name):
    context = {
        "name": name
    }
    return render(request, "contact.html", context)

# def createArticle(request): 
#     title = "Articulo 1"
#     existingArticle = models.Article.objects.filter(title=title)
    
#     if existingArticle.exists():
#         article = updateArticleByTitle(title, existingArticle.exists())
#         context = {
#             "article": article,
#             "exists": "Ya existia en la base de datos"
#         }
#         return render(request, "createArticle.html", context)
#     else:
#         article = models.Article(
#             title="Articulo 1",
#             content="Contenido del articulo 1",
#             public=True
#         )
#         article.save()
#         context = {
#             "article": article
#         }
#         return render(request, "createArticle.html", context)

# def saveArticle(request):
#     if (request.method == "GET"):
#         title = request.GET.get("title")
#         content = request.GET.get("content")
#         public = request.GET.get("public")
#         image = request.GET.get("image")
        
#         if public == "1":
#             public = True
#         else:
#             public = False
        
#         article = models.Article(
#             title=title,
#             content=content,
#             public=public,
#             image=image
#         )
#         article.save()
#         return redirect("index")
#     elif (request.method == "POST"):
#         title = request.POST.get("title")
#         content = request.POST.get("content")
#         public = request.POST.get("public")
#         image = request.POST.get("image")
        
#         if public == "1":
#             public = True
#         else:
#             public = False
        
#         article = models.Article(
#             title=title,
#             content=content,
#             public=public,
#             image=image
#         )
#         article.save()
#         return redirect("index")
#     else: 
#         return redirect("index")

def createArticle(request):
    if (request.method == "POST"):
        formularyArticle = forms.FormularyArticle(request.POST, request.FILES)
        if (formularyArticle.is_valid()):
            dataFormulary = formularyArticle.cleaned_data
            article = models.Article(
                title = dataFormulary.get("title"),
                content = dataFormulary.get("content"),
                public = dataFormulary.get("public"),
                image = dataFormulary.get("image")
            )
            article.save()
            
            messages.success(request, f"Articulo {article.title} creado con exito")
            return redirect("index")
    else:  
        formularyArticle = forms.FormularyArticle()
        return render(request, "createArticle.html", {"formularyArticle": formularyArticle})

# def saveArticle(request):
#     formularyArticle = forms.FormularyArticle()
#     return render(request, "createArticle.html", {"formularyArticle": formularyArticle})
    
def updateArticleByTitle(title, existingArticle) -> object:
    if (existingArticle):
        article = models.Article.objects.get(title=title)
        article.title = "Articulo 1 - Actualizado"
        article.content = "Contenido del articulo 1 - Actualizado"
        article.public = False
        article.save()
        return article
    else: 
        return None
    
def deleteArticleById(request, id):
    article = models.Article.objects.filter(id=id)
    if (article.exists()):
        article.get().delete()
        return redirect("index")
    else: 
        return redirect("index")