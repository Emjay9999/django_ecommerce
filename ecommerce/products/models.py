from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	description = models.CharField(max_length=1000)
	image = models.ImageField(default="default.png", upload_to="product_images")


	def __str__(self):
		return self.name

