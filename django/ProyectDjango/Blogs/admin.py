from typing import Any
from django.contrib import admin
from Blogs import models

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('createDate', 'updateDate')
    search_fields = ('name', 'createDate')
    list_filter = ('name',)
    list_display = ( 'name', 'createDate',)
    #ordering = ('-createDate',)
    
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('createDate', 'updateDate', "user")
    search_fields = ('user__first_name', 'title',)
    list_filter = ('public', "user__first_name", "categories")
    list_display = ("title", "user", "public", 'createDate')
    #ordering = ('-createDate',)
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any):
        if not obj.user_id:
            obj.user_id = request.user.id
        
        obj.save()

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)

title = "Blogs Django - Juan Pablo Leon F"
subTitle = "Panel De Gestion"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subTitle