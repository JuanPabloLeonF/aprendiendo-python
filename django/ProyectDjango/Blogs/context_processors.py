from Blogs import models

def getCategories(request):
    categoriesInUse = models.Article.objects.filter(public=True).values_list("categories", flat=True)
    lisCategories = models.Category.objects.filter(id__in=categoriesInUse).values_list("id", "name")
    return {
        "lisCategories": lisCategories,
        "ids": categoriesInUse
    }