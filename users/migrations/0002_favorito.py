# Generated by Django 5.0.3 on 2024-06-15 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receta_id', models.IntegerField()),
                ('imagen_url', models.URLField()),
                ('descripcion', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritos', to='users.user')),
            ],
        ),
    ]