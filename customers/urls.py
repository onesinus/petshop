from django.urls import path
from customers import views

urlpatterns = [
    path('', views.CustomerList.as_view(), name='customer-list'),
    path('detail/<int:pk>', views.CustomerDetail.as_view(), name='customer-detail'),
    path('create', views.CustomerCreate.as_view(), name='customer-create'),
    path('edit/<int:pk>', views.CustomerEdit.as_view(), name='customer-edit'),
    path('delete/<int:pk>', views.CustomerDelete.as_view(), name='customer-delete')
]