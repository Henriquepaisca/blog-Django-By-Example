from django import forms

from .models import Post


class PostForm(forms.ModelForm): # Nome do nosso formulario

        class Meta: # modelo usado para criar este formulario

        model = Post
        fields = ('title', 'text',)  # title e text exposto
