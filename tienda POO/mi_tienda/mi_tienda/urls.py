"""
URL configuration for mi_tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# mi_tienda_proyecto/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tienda.views import home, registro_usuario, logged_out, producto_crear, producto_editar, producto_eliminar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', registro_usuario, name='registro'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', home, name='home'),
    path('cerrar-sesion/', logged_out, name='logged_out'),


    # --- CRUD de productos ---
    path('producto/nuevo/', producto_crear, name='producto_crear'),
    path('producto/<int:pk>/editar/', producto_editar, name='producto_editar'),
    path('producto/<int:pk>/eliminar/', producto_eliminar, name='producto_eliminar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
