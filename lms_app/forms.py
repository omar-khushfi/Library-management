from django import forms
from .models import *
class categoryform(forms.ModelForm):
    class Meta:
        model=category;
        fields=[
            'name',
        ]
        widgets= {
        'name':forms.TextInput(attrs={'class':'form-control'}),

        }
        
class bookforms(forms.ModelForm):
    class Meta:
        model=book;
        fields=[
            'category',
            'title',
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'price',
            'retal_price_day',
            'retal_period',
            'active',
            'state',
            'total_rental',
           ]
        widgets= {
        'category':forms.Select(attrs={'class':'form-control'}),
         'title':forms.TextInput(attrs={'class':'form-control'}),
          'author':forms.TextInput(attrs={'class':'form-control'}),
           'photo_book':forms.FileInput(attrs={'class':'form-control'}),
            'photo_author':forms.FileInput(attrs={'class':'form-control'}),
             'pages':forms.NumberInput(attrs={'class':'form-control'}),
              'price':forms.NumberInput(attrs={'class':'form-control'}),
               'retal_price_day':forms.NumberInput(attrs={'class':'form-control','id':'rentalprice'}),
                'retal_period':forms.NumberInput(attrs={'class':'form-control','id':'rentaldays'}),
                 'active':forms.TextInput(attrs={'class':'form-control'}),
                  'state':forms.Select(attrs={'class':'form-control'}),
                   'total_rental':forms.NumberInput(attrs={'class':'form-control','id':'totalrental'}),

        }