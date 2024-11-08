# Generated by Django 5.1.2 on 2024-11-05 08:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('sexo', models.CharField(choices=[('M', 'Macho'), ('H', 'Hembra')], max_length=1)),
                ('raza', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kg', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('trazabilidad', models.CharField(blank=True, max_length=200, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('draft', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.post')),
            ],
        ),
    ]
