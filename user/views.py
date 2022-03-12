from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, CustomerForm, OrderForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .models import Product, Customer, Order
from .forms import ProductForm
from django.shortcuts import redirect, render,HttpResponse

def index(request):
	return render(request, 'index.html', {'title':'OSM'})

def image_request(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			img_object = form.instance
			return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})
	else:
		form = ProductForm()

	return render(request, 'image_form.html', {'form': form})

def load_product_form(request):
	form = ProductForm
	return render(request,"add_product.html",{'form':form})

def load_customer_form(request):
	form = CustomerForm
	return render(request,"add_customer.html",{'form':form})

def load_order_form(request):
	form = OrderForm

	return render(request,"add_order.html",{'form':form})

def add(request):
	pro = Product()
	pro.name = request.POST.get('name')
	pro.pro_quantity = request.POST.get('pro_quantity')
	pro.pro_price = request.POST.get('pro_price')
	pro.description = request.POST.get('description')
	pro.save()
	return redirect('products')

def addC(request):
	cus = Customer()
	cus.first_name = request.POST.get('first_name')
	cus.last_name = request.POST.get('last_name')
	cus.address = request.POST.get('address')
	cus.phone_num = request.POST.get('phone_num')
	cus.save()
	return redirect('customers')

def addO(request):
	ord = Order()
	ord.product = Product.objects.get(id=request.POST.get('product'))
	ord.customer = Customer.objects.get(id=request.POST.get('customer'))
	ord.ord_quantity = request.POST.get('ord_quantity')
	ord.ord_price = request.POST.get('ord_price')
	ord.save()
	product = Product.objects.get(id=request.POST.get('product'))
	if int(ord.ord_quantity) > int(product.pro_quantity):
		return render(request, 'show_msg.html')
	else:
		product.pro_quantity = int(product.pro_quantity) - int(ord.ord_quantity)
		product.save()
	return redirect('orders')

def edit(request, id):
	product = Product.objects.get(id=id)
	return render(request,'edit.html',{'product':product})

def editC(request, id):
	customer = Customer.objects.get(id=id)
	return render(request,'editC.html',{'customer':customer})

def editO(request, id):
	order = Order.objects.get(id=id)
	return render(request,'editO.html',{'order':order})

def update(request, id):
	product = Product.objects.get(id=id)
	product.name = request.POST.get('name')
	product.pro_quantity = request.POST.get('pro_quantity')
	product.pro_price = request.POST.get('pro_price')
	product.description = request.POST.get('description')
	product.save()
	return redirect('products')


def updateC(request, id):
	customer = Customer.objects.get(id=id)
	customer.first_name = request.POST.get('first_name')
	customer.last_name = request.POST.get('last_name')
	customer.address = request.POST.get('address')
	customer.phone_num = request.POST.get('phone_num')
	customer.save()
	return redirect('customers')

def updateO(request, id):
	order = Order.objects.get(id=id)
	order.product = request.POST.get('product')
	order.customer = request.POST.get('customer')
	order.ord_quantity = request.POST.get('ord_quantity')
	order.ord_price = request.POST.get('ord_price')
	order.save()
	return redirect('orders')

def delete(request, id):
	Product.objects.filter(id=id).delete()
	return redirect('products')

def deleteC(request, id):
	Customer.objects.filter(id=id).delete()
	return redirect('customers')

def deleteO(request, id):
	Order.objects.filter(id=id).delete()
	return redirect('orders')

def search(request):
	given_name = request.POST['name']
	product = Product.objects.filter(name__icontains=given_name)
	return render(request, 'show_product.html', {'product': product})

def searchC(request):
	given_name = request.POST['name']
	customer = Customer.objects.filter(first_name__icontains=given_name)
	return render(request, 'show_customer.html', {'customer': customer})

def products(request):
	product = Product.objects.all()
	return render(request,'show_product.html',{'product':product})

def customers(request):
	customer = Customer.objects.all()
	return render(request, 'show_customer.html', {'customer': customer})

def orders(request):
	order = Order.objects.all().order_by('-id')
	return render(request,'show_order.html',{'order':order})

def show_product_view(request):
	return render(request,'productV.html')

def show_customer_view(request):
	return render(request, 'customerV.html')

def show_order_view(request):
	return render(request, 'orderV.html')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST) or None
		if form.is_valid():
			username = request.POST.get('username')
			#########################mail####################################
			htmly = get_template('Email.html')
			d = {'username': username}
			subject, from_email, to = 'hello', 'from@example.com', 'to@emaple.com'
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			try:
				msg.send()
			except:
				print("Error in sending mail")
			##################################################################
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', {'form': form, 'title': 'reqister here'})

def Login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' Welcome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'Account does not exist')
	form = AuthenticationForm()
	return render(request, 'login.html', {'form':form, 'title':'Log in'})
# def updatepro(request,id):
