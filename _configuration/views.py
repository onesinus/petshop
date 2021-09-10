from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


class HomeView(TemplateView):
    template_name = "_common/home.html"