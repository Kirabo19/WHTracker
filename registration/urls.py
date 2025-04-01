from django.urls import path
from .views import vehicle_list, vehicle_create, vehicle_update, vehicle_delete

urlpatterns = [
    path('', vehicle_list, name='vehicle_list'),
    path('create/', vehicle_create, name='vehicle_create'),
    path('update/<int:pk>/', vehicle_update, name='vehicle_update'),
    path('delete/<int:pk>/', vehicle_delete, name='vehicle_delete'),
]
