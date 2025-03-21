from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class AccountManager(BaseUserManager):
    def create_user(self, username, email, direccion, telephone, password=None):
        if not username:
            raise Exception("El usuario debe tener un username")
        if not email:
            raise Exception("El usuario debe tener un correo")
        if password is None:
            raise Exception("El usuario debe tener un contrasena")
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            direccion = direccion,
            telephone = telephone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, direccion, telephone, password=None):
        user = self.create_user(
            username=username,
            email=email,
            direccion=direccion,
            telephone=telephone,
            password=password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

        

class Account(AbstractBaseUser):
    #campos propios del negocio
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=50, unique=True)
    direccion = models.TextField(max_length=255)
    telephone = models.CharField(max_length=8)


    #campos de django
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS= ['username', 'direccion', 'telephone']

    objects = AccountManager()

    def __str__(self):
        return f'{self.username}'
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
             
        
    def has_module_perms(self, app_label):
        return True
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)