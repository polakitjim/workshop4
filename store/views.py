from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Employee
from .forms import ProductForm

# Home / Dashboard Page
def home(request):
    total_products = Product.objects.count()
    total_employees = Employee.objects.count()
    recent_products = Product.objects.all().order_by('-id')[:4]
    
    context = {
        'total_products': total_products,
        'total_employees': total_employees,
        'recent_products': recent_products,
    }
    return render(request, 'store/home.html', context)

# Read & Search & Pagination
def product_list(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(name__icontains=query).order_by('-id')
    else:
        products = Product.objects.all().order_by('-id')

    paginator = Paginator(products, 5) # แบ่งหน้าละ 5 รายการ
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'store/product_list.html', {'page_obj': page_obj, 'query': query})

# Create
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form, 'action': 'เพิ่มข้อมูล'})

# Update
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_form.html', {'form': form, 'action': 'แก้ไขข้อมูล'})

# Delete
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'store/product_confirm_delete.html', {'product': product})

# Employee Views
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'store/employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST['name'],
            position=request.POST['position'],
            salary=request.POST['salary'],
            email=request.POST['email'],
            hire_date=request.POST['hire_date']
        )
        return redirect('employee_list')
    return render(request, 'store/employee_create.html')