import sys
from django.db import models
from django.conf import settings
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import date
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Category(models.Model):
	name = models.CharField(max_length=200,db_index=True)
	slug = models.SlugField(max_length=200,unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

class Item(models.Model):
	Categories= (

		('Select category', 'Select Category'),
		('Laptops', 'Laptops'),
		('Phones', 'Phones'),
		('House equipments', 'House equipments'),
		('Electronics', 'Electronics'),
		('Clothes', 'Clothes'),
		('Shoes', 'Shoes'),
		('Stationary', 'Stationary'),
			)

	item_name = models.CharField(max_length=100, null=False)
	item_description = models.TextField(max_length=100, null=False)
	item_price = models.IntegerField(null=False)
	item_image = models.ImageField(upload_to='items')
	item_owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=get_user_model(), on_delete=models.CASCADE)
	item_category = models.CharField(max_length=20, choices=Categories, default=0)
	date_created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.item_name


	def get_absolute_url(self):
		return reverse("item_view:item_detail", args={self.item_name})

	def save(self, *args, **kwargs):


			self.item_image = self.compressImage(self.item_image)

			super(Item, self).save(*args, **kwargs)


	def compressImage(self, item_image):
		ImageTemproary = Image.open(item_image)
		outputIoStream  = BytesIO()
		ImageTemproaryResized = ImageTemproary.resize((600, 650))

		ImageTemproaryResized.save(outputIoStream, format='JPEG', quality=60)
		outputIoStream.seek(0)

		item_image = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % item_image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)


		return  item_image

class Comments(models.Model):

	item = models.CharField(max_length=100, null=False)
	comment = models.TextField(max_length=100, null=False)
	full_name = models.CharField(max_length=100, null=False)
	email = models.CharField(max_length=100, null=True)
	phone_number = models.IntegerField(null=False)
	date_created = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse("item_view:item_comment", args={self.item})

class Replies(models.Model):
	comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
	reply = models.TextField(max_length=100, null=False)
	full_name = models.CharField(max_length=100, null=False)
	email = models.CharField(max_length=100, null=True)
	phone_number = models.IntegerField(null=False)
	date_created = models.DateTimeField(auto_now_add=True)
