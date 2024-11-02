from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Animal

from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
def index(request):
   # Obtener los 10 animales más recientes
    animales_recientes = Animal.objects.filter(draft=False).order_by('-created_at')[:10]
    
    context = {
        'animales': animales_recientes
    }
    
    return render(request, 'home.html', context)
    
def detail_post(request, pk):
   # Obtener los 10 animales más recientes
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'detail_post.html', {'animal': animal})

# @login_required
# def profile(request):
#     return render(request, 'profile.html')

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    context = {
        'user': user,
        'is_owner': request.user.id == user.id  # Check if the logged-in user is the profile owner
    }
    return render(request, 'profile.html', context)

from .forms import AnimalForm

@login_required
def create_post(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            # Asignar el vendedor como el usuario que está realizando el submit
            publicacion = form.save(commit=False)
            publicacion.vendedor = request.user  # Establece el vendedor como el usuario actual
            publicacion.save()
            return redirect('home')  # Cambia esto a tu URL deseada
    else:
        form = AnimalForm()
    
    return render(request, 'create_post.html', {'form': form})
