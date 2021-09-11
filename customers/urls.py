from django.urls import path
from customers.views import customer, customer_discount

urlpatterns = [
    path('', customer.CustomerList.as_view(), name='customer-list'),
    path('detail/<int:pk>', customer.CustomerDetail.as_view(), name='customer-detail'),
    path('create', customer.CustomerCreate.as_view(), name='customer-create'),
    path('edit/<int:pk>', customer.CustomerEdit.as_view(), name='customer-edit'),
    path('delete/<int:pk>', customer.CustomerDelete.as_view(), name='customer-delete'),

    path('discount', customer_discount.CustomerDiscountList.as_view(), name='customer-discount-list'),
    path('discount/detail/<int:pk>', customer_discount.CustomerDiscountDetail.as_view(), name='customer-discount-detail'),
    path('discount/create', customer_discount.CustomerDiscountCreate.as_view(), name='customer-discount-create'),
    path('discount/edit/<int:pk>', customer_discount.CustomerDiscountEdit.as_view(), name='customer-discount-edit'),
    path('discount/delete/<int:pk>', customer_discount.CustomerDiscountDelete.as_view(), name='customer-discount-delete'),

]