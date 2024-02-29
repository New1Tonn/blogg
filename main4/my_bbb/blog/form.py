from django import forms
from .models import Comments

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments  # Замените Comments на вашу модель, если она другая
        fields = ['text_comments', 'name', 'email']  # Убедитесь, что поля указаны корректно

