from django.shortcuts import render

# Create your views here.
def index(request):
    return ""


# Vista para listar y crear publicaciones
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

    def perform_create(self, serializer):
        # Asigna automáticamente el usuario autenticado al campo 'user' del Post
        serializer.save(user=self.request.user)


# Vista para obtener, actualizar, o eliminar una publicación
class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
