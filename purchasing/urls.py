from django.urls import path
from purchasing.views import purchase

urlpatterns = [
    path('', purchase.PurchaseOrderList.as_view(), name='purchase-list'),
    path('detail/<str:pk>', purchase.PurchaseOrderDetail.as_view(), name='purchase-detail'),
    path('create', purchase.PurchaseOrderCreate.as_view(), name='purchase-create'),
    path('edit/<str:pk>', purchase.PurchaseOrderEdit.as_view(), name='purchase-edit'),
    path('delete/<str:pk>', purchase.PurchaseOrderDelete.as_view(), name='purchase-delete')
]