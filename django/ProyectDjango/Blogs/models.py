from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import uuid

class Category(models.Model):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Id"
    )
    
    name = models.CharField(
        verbose_name="Nombre",
        max_length=100
    )
    
    description = models.TextField(
        verbose_name="Descripción",
        max_length=255
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
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return f"{self.name}"
    
    
class Article(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Id"
    )
    
    title = models.CharField(
        verbose_name="Título",
        max_length=100
    )
    
    content = RichTextField(
        verbose_name="Contenido"
    )
    
    image = models.ImageField(
        verbose_name="Imagen",
        upload_to="blogs",
        default="null",
        null=True,
        blank=True
    )
    
    public  = models.BooleanField(
        verbose_name="Publicado"
    )
    
    createDate = models.DateTimeField(
        verbose_name="Fecha de creación",
        auto_now_add=True
    )
    
    updateDate = models.DateTimeField(
        verbose_name="Fecha de actualización",
        auto_now=True
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Usuario",
        editable=False
    )
    
    categories = models.ManyToManyField(
        Category,
        verbose_name="Categorías",
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        
    def __str__(self):
        return f"{self.title}"