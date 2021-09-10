from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from customers.models import Customer
from customers.forms import CustomerForm


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
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by_id = self.request.user.id
        object.save()
        return super(CustomerCreate, self).form_valid(form)


class CustomerEdit(UpdateView):
    model = Customer
    template_name = "customers/form.html"
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.updated_by_id = self.request.user.id
        object.save()
        return super(CustomerEdit, self).form_valid(form)


class CustomerDelete(DeleteView):
    model = Customer
    template_name = "customers/delete.html"
    success_url = reverse_lazy('customer-list')

