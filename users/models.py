from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d')
    date_berth = models.DateTimeField(blank=True, null=True, verbose_name="Date of Birth")
    bio = models.TextField(blank=True, null=True, verbose_name="Biography")
