from django.db import models
from ckeditor.fields import RichTextField
import uuid

class Page(models.Model):
    
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
            unique=True,
            verbose_name="Identificador"
        )
    
    title = models.CharField(
            verbose_name="Título", 
            max_length=50
        )
    
    content = RichTextField(
            verbose_name="Contenido"
        )
    
    slug = models.CharField(
            verbose_name="URL amigable",
            max_length=150,
            unique=True
        )
    
    order = models.IntegerField(
            verbose_name="Orden",
            default=0
    )
    
    visible = models.BooleanField(
            verbose_name="Visible"
        )
    
    createDate = models.DateTimeField(
            verbose_name="Fecha de creación",
            auto_now_add=True
        )
    
    updateDate = models.DateTimeField(
            verbose_name="Fecha de actualización",
            auto_now=True
        )
    
    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
    
    def __str__(self):
        return f"{self.title}"