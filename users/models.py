from django.db import models

class User(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    education_level = models.CharField(max_length=30)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.name} {self.last_name}"
    
class Favorito(models.Model):
    receta_id = models.IntegerField()
    imagen_url = models.URLField(max_length=200)
    descripcion = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos')

    def __str__(self):
        return f"Favorito {self.receta_id} de {self.user.name} {self.user.last_name}"
