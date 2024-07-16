from django import forms
from .models import Barcode

class BarcodeForm(forms.ModelForm):
    class Meta:
        model = Barcode
        fields = ['code']
