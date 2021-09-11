from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from customers.models import CustomerDiscount
from customers.forms.customer_discount import CustomerDiscountForm


class CustomerDiscountList(LoginRequiredMixin, ListView):
    model = CustomerDiscount
    template_name = "customers/discount/list.html"


class CustomerDiscountDetail(LoginRequiredMixin, UpdateView):
    model = CustomerDiscount
    template_name = "customers/discount/detail.html"
    fields = [ 'id', 'customer', 'product', 'is_percentage', 'discount']


class CustomerDiscountCreate(LoginRequiredMixin, CreateView):
    model = CustomerDiscount
    template_name = "customers/discount/form.html"
    form_class = CustomerDiscountForm
    success_url = reverse_lazy('customer-discount-list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by_id = self.request.user.id
        object.save()

        messages.success(self.request, 'Customer Discount has been added.')
        return super(CustomerDiscountCreate, self).form_valid(form)


class CustomerDiscountEdit(LoginRequiredMixin, UpdateView):
    model = CustomerDiscount
    template_name = "customers/discount/form.html"
    form_class = CustomerDiscountForm
    success_url = reverse_lazy('customer-discount-list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.updated_by_id = self.request.user.id
        object.save()

        messages.success(self.request, 'Customer Discount has been updated.')
        return super(CustomerDiscountEdit, self).form_valid(form)


class CustomerDiscountDelete(LoginRequiredMixin, DeleteView):
    model = CustomerDiscount
    template_name = "customers/discount/delete.html"
    success_url = reverse_lazy('customer-discount-list')
    success_message = "Customer Discount has been deleted"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CustomerDiscountDelete, self).delete(request, *args, **kwargs)