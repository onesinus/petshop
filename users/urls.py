from django.urls import path
from users import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('detail/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    # path('create', views.UserCreate.as_view(), name='user-create'),
    # path('edit/<int:pk>', views.UserCreate.as_view(), name='user-edit')
]