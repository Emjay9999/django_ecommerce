from django.urls import path
from . import views


urlpatterns = [
	path('index/', views.index, name="index"),
	path('product_list/', views.product_list, name="product_list"),
	path('add_product/', views.add_product, name="add_product"),
	path('update_product/<int:pk>/', views.update_product, name="update_product"),
	path('delete_product/<int:pk>/', views.delete_product, name="delete_product"),
	path('add_cart/', views.add_cart, name="add_cart"),
	path('empty_cart/', views.empty_cart, name="empty_cart"),
	path('details/<int:pk>/', views.details, name="details"),


]