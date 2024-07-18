from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d')
    date_berth = models.DateTimeField(blank=True, null=True, verbose_name=_("Date of Birth"))
    bio = models.TextField(blank=True, null=True, verbose_name=_("Biography"))
