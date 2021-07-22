from .models import *
from django import forms

class CityForm(forms.ModelForm):
    class Meta:
        model=City
        fields=['name']
        labels={
            'name':'Enter Your City:'
        }
    
    def __init__(self,*args,**kwargs):
        super(CityForm,self).__init__(*args,**kwargs)
        self.fields['name'].required=False