from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')  # columnas en la tabla
    search_fields = ('name',)              # barra de búsqueda
