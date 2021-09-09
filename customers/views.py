from django.views.generic import TemplateView, DetailView, FormView
from customers.models import Customer


class CustomerList(TemplateView):
    template_name = "customers/list.html"


class CustomerDetail(DetailView):
    template_name = "customers/detail.html"
    model = Customer

# class CustomerCreate(FormView):
#     template_name = "customers/form.html"
#     model = Customer

# class CustomerEdit(FormView):
#     template_name = "customers/form.html"
#     model = Customer