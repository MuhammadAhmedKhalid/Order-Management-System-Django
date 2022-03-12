from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from .models import Customer
from .models import Order
from .models import UploadImage

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone_no = forms.CharField(max_length = 20)
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	class Meta:
		model = User
		fields = ['username', 'email', 'phone_no', 'password1', 'password2']

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
		# ordering = [-1]

class UserImage(forms.ModelForm):
	class meta:
		# To specify the model to be used to create form
		models = UploadImage
		# It includes all the fields of model
		fields = '__all__'