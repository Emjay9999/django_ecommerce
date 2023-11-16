from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
	myproducts = Product.objects.all()

	context = {
		"myproducts":myproducts
		
	}
	return render(request, "hello.html", context)


def contact(request):
	context = {

	}
	return render(request, "contacts.html", context)
