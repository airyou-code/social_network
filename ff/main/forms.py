from django import forms
from user.models import User


class DocumentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('profImg', )
