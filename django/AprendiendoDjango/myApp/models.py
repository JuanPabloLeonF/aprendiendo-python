from django.db import models
import uuid

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="ID")
    title = models.CharField(max_length=100, verbose_name="TITULO")
    content = models.TextField(verbose_name="CONTENIDO")
    image = models.ImageField(blank=True, null=True, verbose_name="IMAGEN", upload_to="articles")
    public = models.BooleanField(verbose_name="PUBLICADO")
    dateCreate = models.DateTimeField(auto_now_add=True, verbose_name="FECHA DE CREACIÓN")
    dateUpdate = models.DateTimeField(auto_now_add=True, verbose_name="FECHA DE ACTUALIZACIÓN")
    
    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        
    def __str__(self) -> str:
        if self.public:
            public = "(PUBLICO)"
        else:
            public  = "(PRIVADO)"
        return f"{self.title} - {public}"

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name="ID")
    name = models.CharField(max_length=100, verbose_name="NOMBRE")
    description = models.TextField(verbose_name="Descripción")
    dateCreate = models.DateTimeField(auto_now_add=True, verbose_name="FECHA DE CREACIÓN")
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'