from rest_framework import serializers
from .models import User,Favorito


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ('id', 'user','password','name','last_name','education_level','birthdate')

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Favorito
        fields = ('id', 'receta_id','imagen_url','descripcion','user')