from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):

    def create_user(self, email, user_name, password, **extra_fields ):
        if not email:
            raise ValueError(_('You must provide email'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,  **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, password , **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, user_name, password ,**extra_fields )


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=30, unique=True, default='user')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now())

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['user_name']

    objects = CustomAccountManager()


    def __str__(self):
        return self.email