"""OSM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from user import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('user.urls')),
	path('login/', user_view.Login, name ='login'),
	path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
	path('register/', user_view.register, name ='register'),
	path('load_product_form',user_view.load_product_form, name='load_product_form'),
	path('load_customer_form',user_view.load_customer_form, name='load_customer_form'),
	path('load_order_form',user_view.load_order_form, name='load_order_form'),
	path('add',user_view.add,name='add'),path('orders',user_view.orders,name='orders'),
	path('addC',user_view.addC,name='addC'),path('addO',user_view.addO,name='addO'),
	path('products',user_view.products,name='products'),path('customers',user_view.customers,name='customers'),
	path('show_product_view',user_view.show_product_view,name='show_product_view'),
	path('show_customer_view',user_view.show_customer_view,name='show_customer_view'),
	path('show_order_view',user_view.show_order_view,name='show_order_view'),
	path('edit/<int:id>',user_view.edit),path('editC/<int:id>',user_view.editC),
	path('editO/<int:id>',user_view.editO),path('update/<int:id>',user_view.update),
	path('updateC/<int:id>',user_view.updateC),path('updateO/<int:id>',user_view.updateO),
	path('delete/<int:id>',user_view.delete),path('deleteC/<int:id>',user_view.deleteC),
	path('deleteO/<int:id>',user_view.deleteO),path('search',user_view.search),
	path('searchC',user_view.searchC),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)