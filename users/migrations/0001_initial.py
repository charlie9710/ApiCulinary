# Generated by Django 5.0.3 on 2024-06-14 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('education_level', models.CharField(max_length=30)),
                ('birthdate', models.DateField()),
            ],
        ),
    ]
