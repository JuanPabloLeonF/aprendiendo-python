from django.contrib import admin
from Pages import models

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('createDate', 'updateDate')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'createDate')
    #ordering = ('-createDate',)

admin.site.register(models.Page, PageAdmin)

title = "Proyectos Django - Juan Pablo Leon F"
subTitle = "Panel De Gestion"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subTitle