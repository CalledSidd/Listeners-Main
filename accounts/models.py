from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here. 
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, phone_number, password):
        if not email:
            raise ValueError("user must have an email address")

        if not username:
            raise ValueError("User must have username")

        user = self.model(
            email      = self.normalize_email(email),
            username   = username,
            first_name = first_name,
            last_name  = last_name,
            phone_number = phone_number,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using= self._db)
        return user   
    
    def create_superuser(self, first_name,last_name, email, username, password,phone_number):
        user = self.create_user(
            email        = self.normalize_email(email),
            username     = username,
            password     = password,
            first_name   = first_name,
            last_name    = last_name,
            phone_number = phone_number,
        )
        user.is_admin      = True
        user.is_active     = True
        user.is_staff      = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name    =  models.CharField(max_length=50)
    last_name     =  models.CharField(max_length=50)
    username      =  models.CharField(max_length=50 , unique = True)
    email         = models.EmailField(max_length=100 , unique=True)
    phone_number  = models.CharField(max_length=50,null = True, blank=True)
    # address       = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    #required
    date_joined   = models.DateTimeField(auto_now_add=True)
    last_login    = models.DateTimeField(auto_now_add=True)
    is_admin      =  models.BooleanField(default=False)
    is_staff      =  models.BooleanField(default=False)
    is_active     =  models.BooleanField(default=True)
    is_superadmin =  models.BooleanField(default=False)
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','phone_number']
    
    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True


class Address(models.Model):
    user            = models.ForeignKey(Account,on_delete=models.CASCADE, null=True)
    firstname       = models.CharField(max_length=50, null=True)
    lastname        = models.CharField(max_length=50, null=True)
    phonenumber     = models.CharField(max_length=50, null=True)
    address         = models.CharField(max_length=50, null=True)
    email           = models.CharField(max_length=50, null=True)
    town            = models.CharField(max_length=50, null=True)
    state           = models.CharField(max_length=50, null=True)
    pincode         = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.firstname