from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('IT', 'อุปกรณ์ไอที'),
        ('OFFICE', 'เครื่องใช้สำนักงาน'),
        ('BOOK', 'หนังสือ'),
    )

    name = models.CharField(max_length=100, verbose_name="ชื่อสินค้า")
    description = models.TextField(verbose_name="รายละเอียด")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ราคา")
    stock = models.IntegerField(verbose_name="จำนวนในสต็อก")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="หมวดหมู่")
    created_date = models.DateField(auto_now_add=True, verbose_name="วันที่เพิ่มข้อมูล")
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="รูปภาพสินค้า")

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name="ชื่อ-นามสกุล")
    position = models.CharField(max_length=50, verbose_name="ตำแหน่ง")
    salary = models.IntegerField(verbose_name="เงินเดือน")
    email = models.EmailField(verbose_name="อีเมล")
    hire_date = models.DateField(verbose_name="วันที่เริ่มงาน")
    photo = models.ImageField(upload_to='employees/', null=True, blank=True, verbose_name="รูปพนักงาน")

    def __str__(self):
        return self.name