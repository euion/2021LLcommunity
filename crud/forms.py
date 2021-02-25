from django import forms
from .models import Crud, Info,  Qna

class CrudUpdate(forms.ModelForm):
    class Meta:
        model = Crud
        fields = ['title', 'body', 'name']

class InfoUpdate(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['title', 'body', 'name']

class QnaUpdate(forms.ModelForm):
    class Meta:
        model = Qna
        fields = ['title', 'body', 'name']

