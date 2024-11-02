from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Animal(models.Model):

    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicaciones')

    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('H', 'Hembra'),
    ]

    RAZA_CHOICES = [
        ('Simmental', 'Simmental'),
        ('Brahman', 'Brahman'),
        ('Jersey', 'Jersey'),
        ('Nelore', 'Nelore'),
        ('Angus', 'Angus'),
        ('Hereford', 'Hereford'),
        ('Holstein', 'Holstein'),
        ('Charolais', 'Charolais'),
        ('Otro', 'Otro'),
    ]

    # Información básica
    imagen = models.ImageField(upload_to='imagenes/', null=True)
    id_animal = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    
    # Parentesco
    madre_id = models.CharField(max_length=20, blank=True)
    padre_id = models.CharField(max_length=20, blank=True)

    # Raza
    raza_principal = models.CharField(max_length=50, choices=RAZA_CHOICES)
    raza_secundaria = models.CharField(max_length=50, choices=RAZA_CHOICES, blank=True)
    raza_terciaria = models.CharField(max_length=50, choices=RAZA_CHOICES, blank=True)
    rasgos_especiales = models.TextField(blank=True)

    # Categoría del animal
    CATEGORIA_CHOICES = [
        ('Destace', 'Destace'),
        ('Exportación', 'Exportación'),
        ('Producción de Leche', 'Producción de Leche'),
        ('Producción de Carne', 'Producción de Carne'),
        ('Producción de Reproducción', 'Producción de Reproducción'),
        ('Venta', 'Venta'),
    ]
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)

    # Información reproductiva
    fecha_nacimiento = models.DateField()
    ultimo_parto = models.DateField(blank=True, null=True)
    fecha_preñez = models.DateField(blank=True, null=True)
    fecha_ultimo_celo = models.DateField(blank=True, null=True)
    dias_preñez = models.IntegerField(blank=True, null=True)
    fecha_esperada_parto = models.DateField(blank=True, null=True)

    # Producción de leche
    produccion_diaria_leche = models.FloatField(blank=True, null=True)
    dias_lactancia = models.IntegerField(blank=True, null=True)
    control_lacteo = models.BooleanField(default=False)

    # Salud y vacunación
    estado_salud = models.TextField(blank=True)
    vacunacion_brucelosis = models.BooleanField(default=False)
    otras_vacunas = models.TextField(blank=True)

    # Indicadores de rendimiento
    peso_actual = models.FloatField()
    edad = models.CharField(max_length=20)  # Meses o años
    entrada_hato = models.DateField(blank=True, null=True)
    iep = models.CharField(max_length=20, blank=True)  # Intervalo entre partos
    iy = models.IntegerField(blank=True, null=True)  # Año de inseminación
    u = models.FloatField(blank=True, null=True)  # Índice de Utilidad

    # Datos de venta o descarte
    para_venta = models.BooleanField(default=False)
    precio_estimado = models.FloatField(blank=True, null=True)

    # Comentarios adicionales
    comentarios = models.TextField(blank=True)

    draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)      # Fecha de última actualización

    def __str__(self):
        return f'{self.nombre} - {self.id_animal}'