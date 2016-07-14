from django import forms

from .models import Post


class NewPostForm(forms.ModelForm):  # Nome do nosso formulario

    class Meta:  # modelo usado para criar este formulario
        model = Post
        fields = ('title', 'body',)  # title e text exposto
