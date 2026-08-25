from django.contrib import admin
from django.urls import path
from store import views  # ดึง views จากแอป store

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # กำหนดให้หน้าแรกสุดชี้ไปที่หน้า home
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
]