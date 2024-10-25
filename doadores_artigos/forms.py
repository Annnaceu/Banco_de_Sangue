from django import forms
from .models import Doador

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['nome', 'idade', 'tipo_sanguineo', 'data_donacao']

