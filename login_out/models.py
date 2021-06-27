from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin,BaseUserManager

# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_user(self , email , username , password):
        if not email:
            raise ValueError('Incorrect Email')
        if not username:
            raise ValueError('Incorrect Username')
        email = self.normalize_email(email)
        user = self.model(email = email , username = username)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self , email , username , password):
        email = self.normalize_email(email)
        user = self.create_user( email = email , username = username , password = password)
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(_('email_address') , unique = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length = 50)

    #required fields
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
	    return self.email

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)  #The foreign key of the user model, the email
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    prefer_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=50)
    school = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username



