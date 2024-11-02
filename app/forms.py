from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):

    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    ultimo_parto = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    fecha_preñez = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    fecha_ultimo_celo = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    fecha_esperada_parto = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    entrada_hato = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)


    class Meta:
        model = Animal
        fields = [
            'imagen',
            'id_animal',
            'nombre',
            'sexo',
            'madre_id',
            'padre_id',
            'raza_principal',
            'raza_secundaria',
            'raza_terciaria',
            'rasgos_especiales',
            'categoria',
            'fecha_nacimiento',
            'ultimo_parto',
            'fecha_preñez',
            'fecha_ultimo_celo',
            'dias_preñez',
            'fecha_esperada_parto',
            'produccion_diaria_leche',
            'dias_lactancia',
            'control_lacteo',
            'estado_salud',
            'vacunacion_brucelosis',
            'otras_vacunas',
            'peso_actual',
            'edad',
            'entrada_hato',
            'iep',
            'iy',
            'u',
            'para_venta',
            'precio_estimado',
            'comentarios',
        ]
