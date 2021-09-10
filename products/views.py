from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from products.models import Product
from products.forms import ProductForm


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/list.html"


class ProductDetail(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "products/detail.html"
    fields = [ 'id', 'code', 'name', 'sales_price']


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "products/form.html"
    form_class = ProductForm
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by_id = self.request.user.id
        object.save()

        messages.success(self.request, 'Product has been added.')
        return super(ProductCreate, self).form_valid(form)


class ProductEdit(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "products/form.html"
    form_class = ProductForm
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.updated_by_id = self.request.user.id
        object.save()

        messages.success(self.request, 'Product has been updated.')
        return super(ProductEdit, self).form_valid(form)


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "products/delete.html"
    success_url = reverse_lazy('product-list')
    success_message = "Product has been deleted"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProductDelete, self).delete(request, *args, **kwargs)