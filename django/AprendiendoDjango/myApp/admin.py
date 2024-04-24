from django.contrib import admin
from myApp import models

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('dateCreate', 'dateUpdate')

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Category)

#Configurar el titulo del panel
title = "Aprendiendo Django - Juan Pablo Leon F"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = title