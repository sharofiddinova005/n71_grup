
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from django.db import models


# class Category(models.Model):
#     title = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.title
#
# class News(models.Model):
#     title = models.CharField(max_length=50)
#     context = models.TextField(blank=True)
#     created_ed = models.DateTimeField(auto_now_add=True)
#     updated_ed = models.DateTimeField(auto_now=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     is_bool = models.BooleanField(default=True)
#     views = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title

from django.db import models
from django.contrib.auth import get_user_model

# Users = get_user_model()


class Actor(models.Model):
    name = models.CharField(max_length=150)
    birthdate = models.DateField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    actor = models.ManyToManyField(Actor)


class CommitMovie(models.Model):
   movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
   title = models.TextField(blank=True,null=True)
   author = models.ForeignKey('User',on_delete=models.CASCADE)



class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Username kiritilishi shart!')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser is_admin=True bo‘lishi kerak!')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser is_staff=True bo‘lishi kerak!')

        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  # Superuser yaratishda email ham so‘raladi

    def __str__(self):
        return self.username

    @property
    def is_superuser(self):
        return self.is_admin

