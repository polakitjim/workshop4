from django.urls import path
from . import views

urlpatterns = [
    # ระบบสินค้า
    path('', views.product_list, name='product_list'),
    path('product/create/', views.product_create, name='product_create'),
    
    # ระบบพนักงาน (เพิ่มส่วนนี้เข้าไป)
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
]