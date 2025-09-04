from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')  # columnas
    list_filter = ('publication_date', 'author')            # filtros laterales
    search_fields = ('title', 'author__name')               # búsqueda
