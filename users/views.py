from django.views.generic import TemplateView, DetailView, FormView
from django.contrib.auth.models import User


class UserList(TemplateView):
    template_name = "users/list.html"


class UserDetail(DetailView):
    template_name = "users/detail.html"
    model = User

# class UserCreate(FormView):
#     template_name = "users/form.html"
#     model = User

# class UserEdit(FormView):
#     template_name = "users/form.html"
#     model = User