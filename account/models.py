from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        Group,
        related_name='CustomUser_set',

        blank=True)
    
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='CustomUser_set_permissions')

    def __str__(self):
        return self.username

class Registration(models.Model):
    image = models.ImageField(upload_to='registration_pics', blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=100, blank=True)
    confirm_password = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_deleted_at = models.DateTimeField(null=True, blank=True)
    last_login = models.DateTimeField(null=True)
    date_joined = models.DateTimeField(null=True)
    is_anonymous = models.BooleanField(default=False)
    username = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    verification_token = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Registration for {self.user.username}"
    

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='userprofile')
    image = models.ImageField(upload_to='profile_pics', blank=True)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    


    