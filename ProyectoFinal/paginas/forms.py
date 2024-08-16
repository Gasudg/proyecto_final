from django import forms
from .models import Pagina

class PaginaForm(forms.ModelForm):
    class Meta:
        model = Pagina
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
        widgets = {
            'cuerpo': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            if not self.user.is_superuser:
                self.fields.pop('imagen')
    
    def clean(self):
        cleaned_data = super().clean()
        if not self.user.is_superuser and 'imagen' in cleaned_data:
            cleaned_data.pop('imagen')
        return cleaned_data
