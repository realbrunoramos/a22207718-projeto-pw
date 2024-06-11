from django import forms
from .models import Artigo

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'conteudo', 'categoria', 'autor', 'data_publicacao']
