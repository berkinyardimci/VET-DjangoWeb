from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):
    name= forms.CharField(widget=forms.TextInput(attrs={
         'class': 'input',
         'placeholder' : 'name'
     }))
    type= forms.CharField(widget=forms.TextInput(attrs={
         'class': 'input',
         'placeholder' : 'type'
     }))

    genus= forms.CharField(widget=forms.TextInput(attrs={
         'class': 'input',
         'placeholder' : 'Cins'
     }))

    age= forms.CharField(widget=forms.NumberInput(attrs={
         'class': 'input',
         'placeholder' : 'age'
     })) 

    description= forms.CharField(widget=forms.TextInput(attrs={
         'class': 'input',
         'placeholder' : 'description'
     }))
    image= forms.CharField(widget=forms.FileInput(attrs={
         'class': 'input',
         'placeholder' : 'image'
     }))        

    class Meta:
        model = Animal
        fields = ['name','type','genus','age','description','image']