from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import *

# Create your models here.
class CustomUser(AbstractBaseUser):
    username=None
    email=models.EmailField(unique=True)
    nid=models.IntegerField()
    is_nid_verified=models.BooleanField(default=False)
    
    objects=UserManager
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
