from django.contrib import admin
from tiendaApp.models import Productos

# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display=['id', 'Nserie', 'NomProducto', 'Descripcion', 'Cantidad', 'Categoria','Precio']

admin.site.register(Productos,ProductosAdmin)
