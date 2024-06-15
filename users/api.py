from users.models import User,Favorito
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, FavoritoSerializer


class UserViewSet (viewsets.ModelViewSet):
        queryset = User.objects.all()
        permission_classes = [permissions.AllowAny]
        serializer_class = UserSerializer

class FavoritoViewSet (viewsets.ModelViewSet):
        queryset = Favorito.objects.all()
        permission_classes = [permissions.AllowAny]
        serializer_class = FavoritoSerializer