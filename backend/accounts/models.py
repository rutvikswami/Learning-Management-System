from django.db import models
from .manager import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True, db_index=True)

    user_name = models.CharField(max_length=100)

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('creator', 'Creator'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default='student'
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['user_name']
    
    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.user_name