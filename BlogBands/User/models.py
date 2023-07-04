from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin, BaseUserManager, UserManager


class UserManagerCustom(BaseUserManager):
    def create_user(self,username, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(username=username,email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, email, password, **extra_fields)
    # def create_user(self,username,email,firstname='',lastname='',password=None):
    #     if not email:
    #         raise ValueError('El usuario debe tener un correo electrónico')
        
    #     usuario = self.model(
    #         username=username,
    #         email=self.normalize_email(email),
    #         first_name=firstname,
    #         last_name=lastname
    #     )

    #     usuario.set_password(password)
    #     usuario.save()
    #     return usuario
    
    # def create_superuser(self,username,email,password):
    #     usuario = self.create_user(
    #         username=username,
    #         email=email
    #     )

    #     usuario.is_staff = True
    #     usuario.is_superuser = True
    #     usuario.save()

    #     return usuario

class User(AbstractUser):
    img = models.CharField(max_length=20)
    objects = UserManagerCustom()

    class Meta:
        db_table = 'auth_user'
