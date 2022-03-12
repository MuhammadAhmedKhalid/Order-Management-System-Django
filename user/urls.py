from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import image_request
urlpatterns = [
	path('', views.index, name ='index'),
	path('', image_request, name = "image-request")
]
urlpatterns += staticfiles_urlpatterns()