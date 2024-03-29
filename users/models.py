from django.contrib.auth.models import AbstractUser
from django.db import models

# try upload images:
from django import forms
from django.core.files.images import get_image_dimensions

from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse
from django.shortcuts import render

# Validatore for file size:
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# for email verfication:
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from march import settings

from shop.models import Product
import random
from django.http import JsonResponse
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status

def create_new_ref_number():
      return str(random.randint(1000000000, 9999999999))

def file_size(value):
    limit = 3 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Image too large! Size should not exceed 3 MB.')


class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True)
    province = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to='media/', null=True, blank=True,
                              default='static/images/clipart-travel.jpg', validators=[file_size])
    newsLetter = models.BooleanField(default=False)
    agreement = models.BooleanField(default=True)
    # next 3 line just to let user loggin with email not username:
    email = models.EmailField(unique=True)
    is_vip = models.BooleanField(default=False)
    vip_date_from = models.DateField(null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'username',

    def __str__(self):
        return self.username



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=CustomUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productsWishlist")
    get_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Wishlist"

    def __str__(self):
        return ('name')
