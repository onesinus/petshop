from django.urls import path
from products import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product-list'),
    path('detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('create', views.ProductCreate.as_view(), name='product-create'),
    path('edit/<int:pk>', views.ProductEdit.as_view(), name='product-edit'),
    path('delete/<int:pk>', views.ProductDelete.as_view(), name='product-delete')
]