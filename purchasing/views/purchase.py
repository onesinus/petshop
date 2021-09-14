from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from purchasing.models import PurchaseOrder
from purchasing.forms.purchase import PurchaseOrderForm


class PurchaseOrderList(LoginRequiredMixin, ListView):
    model = PurchaseOrder
    template_name = "purchasing/purchase/list.html"


class PurchaseOrderDetail(LoginRequiredMixin, UpdateView):
    model = PurchaseOrder
    template_name = "purchasing/purchase/detail.html"
    fields = [ 'id', 'product', 'qty', 'capital_price']


class PurchaseOrderCreate(LoginRequiredMixin, CreateView):
    model = PurchaseOrder
    template_name = "purchasing/purchase/form.html"
    form_class = PurchaseOrderForm
    success_url = reverse_lazy('purchase-list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by_id = self.request.user.id
        object.save()

        messages.success(self.request, 'Purchase Order has been added.')
        return super(PurchaseOrderCreate, self).form_valid(form)


class PurchaseOrderEdit(LoginRequiredMixin, UpdateView):
    model = PurchaseOrder
    template_name = "purchasing/purchase/form.html"
    form_class = PurchaseOrderForm
    success_url = reverse_lazy('purchase-list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.updated_by_id = self.request.user.id
        object.save()

        messages.success(self.request, 'Purchase Order has been updated.')
        return super(PurchaseOrderEdit, self).form_valid(form)


class PurchaseOrderDelete(LoginRequiredMixin, DeleteView):
    model = PurchaseOrder
    template_name = "purchasing/purchase/delete.html"
    success_url = reverse_lazy('purchase-list')
    success_message = "Purchase Order has been deleted"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PurchaseOrderDelete, self).delete(request, *args, **kwargs)