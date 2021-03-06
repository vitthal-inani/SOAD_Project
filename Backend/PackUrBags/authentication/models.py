from djongo import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, phone_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserData(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name = models.CharField(max_length=100, default="first_name")
    last_name = models.CharField(max_length=100, default="last_name")
    username = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=10, default="phone")
    profile_pic = models.ImageField(default='no_image.png', upload_to='user_profile_pics/')
    dob = models.DateField(default=datetime.today)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number', ]

    objects = UserAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender=settings.AUTH_USER_MODEL, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
