from django import forms
from .models import Crud, Info,  Qna

class CrudUpdate(forms.ModelForm):
    class Meta:
        model = Crud
        fields = ['title', 'profile_id', 'body']
        lables = {
        'title':'제목' ,
        'profile_id': '작성자', 
        'body' : '본문'
        }
        widgets = {
            'profile_id' : forms.HiddenInput()
        }
class InfoUpdate(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['title', 'profile_id', 'body']
        lables = {
        'title':'제목' ,
        'profile_id': '작성자', 
        'body' : '본문'
        }
        widgets = {
            'profile_id' : forms.HiddenInput()
        }
class QnaUpdate(forms.ModelForm):
    class Meta:
        model = Qna
        fields = ['title', 'profile_id','body']
        lables = {
        'title':'제목' ,
        'profile_id': '작성자', 
        'body' : '본문'
        }
        widgets = {
            'profile_id' : forms.HiddenInput()
        }
