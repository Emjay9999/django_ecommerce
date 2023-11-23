from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Product
from .forms import ProductForm


def index(request):
	myproducts = Product.objects.all()
	context = {
		"myproducts":myproducts
		
	}
	return render(request, "home.html", context)


def product_list(request):
	products_list = Product.objects.all()
	context ={
		"products_list":products_list
	}
	return render(request, "product_list.html", context)


def add_product(request):
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Product Added Successfully")
			return redirect("product_list")
		else:
			messages.error(request, "Error while adding the product")
	else:
		form = ProductForm
	return render(request, "add_products.html", {"form": form})


def update_product(request, pk):
	instance = get_object_or_404(Product, pk=pk)
	if request.method == "POST":
		form = ProductForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			messages.success(request, "Product updated succesfully")
			return redirect("product_list")
		else:
			messages.error(request, "Unable to update the product")
	else:
		form = ProductForm(instance = instance)

	return render(request, "update_product.html",{"form" : form})


def delete_product(request, pk):
	product = get_object_or_404(Product, pk=pk)
	if request.method == "POST":
		product.delete()
		messages.success(request, "Product Deleted Succesfully")
		return redirect("product_list")

	return render(request, "delete_product.html", {"product":product})

