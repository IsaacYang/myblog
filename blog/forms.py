from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    """Form definition for Comment."""
    class Meta:
        """Meta definition for Commentform."""
        model = Comment
        fields = ('name','email','body')

