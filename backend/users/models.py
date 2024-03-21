from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)