from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from customers.models import Customer


class CustomerList(ListView):
    model = Customer
    template_name = "customers/list.html"


class CustomerDetail(UpdateView):
    model = Customer
    template_name = "customers/detail.html"
    fields = [ 'id', 'name', 'email', 'address']

class CustomerCreate(CreateView):
    model = Customer
    template_name = "customers/form.html"
    fields = [ 'id', 'name', 'email', 'address']

class CustomerEdit(UpdateView):
    model = Customer
    template_name = "customers/form.html"
    fields = [ 'id', 'name', 'email', 'address']

class CustomerDelete(DeleteView):
    model = Customer
    template_name = "customers/delete.html"
    success_url = reverse_lazy('customer-list')

