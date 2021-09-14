from django import forms
from purchasing.models import PurchaseOrder


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ('product', 'qty', 'capital_price')

        widgets = {
            'qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'capital_price': forms.NumberInput(attrs={'class': 'form-control'})
        }