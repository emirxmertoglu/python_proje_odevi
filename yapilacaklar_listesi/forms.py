from django import forms
from .models import yapilacaklarListesi

class yapilacaklarListesiForm(forms.Form):
  yazi = forms.CharField(max_length=40,
    widget = forms.TextInput(
      attrs = {'class' : 'form-control', 'placeholder' : 'Yapılacakları girin, ör. En az 5 makale oku.', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}
    ))

class yeniYapilacaklarListesiForm(forms.ModelForm):
  class Meta:
    model = yapilacaklarListesi
    fields = ['yazi']
    widgets = {
      'yazi' : forms.TextInput(
      attrs = {'class' : 'form-control', 'placeholder' : 'Yapılacakları girin, ör. En az 5 makale oku.', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}
      )
    }