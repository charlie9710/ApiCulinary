from users.models import User,Favorito
from rest_framework import viewsets, permissions, status
from .serializers import UserSerializer, FavoritoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class UserViewSet (viewsets.ModelViewSet):
        queryset = User.objects.all()
        permission_classes = [permissions.AllowAny]
        serializer_class = UserSerializer
        @action(detail=False, methods=['get'])
        def search_by_username(self, request): #/api/users/search_by_username/?username=nombre_usuario
                username = request.query_params.get('username', None)
                print(f"Searching user with username: {username}")
                if username is not None:
                        users = User.objects.filter(user=username)
                        serializer = self.get_serializer(users, many=True)
                        return Response(serializer.data)
                else:
                        return Response({"error": "Please provide a username"}, status=400)
        @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
        def create_user(self, request): #POST /api/users/create_user/
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        @action(detail=False, methods=['put'], permission_classes=[permissions.AllowAny])
        def update_user(self, request):  # PUT /api/users/update_user/?username=nombre_usuario
                username = request.query_params.get('username', None)
                if not username:
                 return Response({"error": "Please provide a username"}, status=status.HTTP_400_BAD_REQUEST)
                user = get_object_or_404(User, user=username)
                serializer = UserSerializer(user, data=request.data, partial=True)
                if serializer.is_valid():            
                 serializer.save()
                 return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FavoritoViewSet (viewsets.ModelViewSet):
        queryset = Favorito.objects.all()
        permission_classes = [permissions.AllowAny]
        serializer_class = FavoritoSerializer

        @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
        def get_favoritos_by_user(self, request, user_id=None): #GET /api/favoritos/user/{user_id}/
                favoritos = Favorito.objects.filter(user_id=user_id)
                serializer = self.get_serializer(favoritos, many=True)
                return Response(serializer.data)

        @action(detail=False, methods=['post'])
        def add_favorito(self, request): #POST /api/favoritos/add_favorito/
                serializer = FavoritoSerializer(data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def destroy(self, request, *args, **kwargs):
                try:
                        instance = self.get_object()
                        self.perform_destroy(instance)
                        return Response(status=status.HTTP_204_NO_CONTENT)
                except Exception as e:
                        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)