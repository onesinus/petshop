from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from customers.models import Customer
from customers.forms import CustomerForm


class CustomerList(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "customers/list.html"


class CustomerDetail(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = "customers/detail.html"
    fields = [ 'id', 'name', 'email', 'address']


class CustomerCreate(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = "customers/form.html"
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by_id = self.request.user.id
        object.save()

        messages.success(self.request, 'Customer has been added.')
        return super(CustomerCreate, self).form_valid(form)


class CustomerEdit(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = "customers/form.html"
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.updated_by_id = self.request.user.id
        object.save()

        messages.success(self.request, 'Customer has been updated.')
        return super(CustomerEdit, self).form_valid(form)


class CustomerDelete(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = "customers/delete.html"
    success_url = reverse_lazy('customer-list')
    success_message = "Customer has been deleted"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CustomerDelete, self).delete(request, *args, **kwargs)