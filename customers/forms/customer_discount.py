from django import forms
from customers.models import CustomerDiscount


class CustomerDiscountForm(forms.ModelForm):
    class Meta:
        model = CustomerDiscount
        fields = ('customer', 'product', 'is_percentage', 'discount')

        widgets = {
            'discount': forms.NumberInput(attrs={'class': 'form-control'})
        }