from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator
from .models import Producto, Categoria

def registro_usuario(request):
    """
    Vista para el registro de nuevos usuarios.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def home(request):
    """
    Vista de la página principal con filtros y paginación.
    """
    productos_list = Producto.objects.all()
    categorias = Categoria.objects.all()

    # Lógica de filtrado por categoría
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        productos_list = productos_list.filter(categoria_id=categoria_id)
        
    # Lógica de paginación (6 productos por página)
    paginator = Paginator(productos_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'page_obj': page_obj,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id,
    })

def logged_out(request):
    return render(request, 'logged_out.html')
#---------
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from .forms import ProductoForm

# Crear producto
def producto_crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form, 'accion': 'Crear'})

# Editar producto
def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form, 'accion': 'Editar'})

# Eliminar producto
def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('home')
    return render(request, 'producto_confirm_delete.html', {'producto': producto})
