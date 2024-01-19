from django.db import models

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    roles = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class File(models.Model):
    name = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

    def __str__(self):
        return self.name


# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     roles = models.CharField(max_length=255)
    
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['roles']


#     def __str__(self):
#         return self.email


#     def is_client(self):
#         return 'client' in self.roles.lower()



# class File(models.Model):
#     # Add necessary fields for your File model, e.g., name, upload_date, etc.
#     name = models.CharField(max_length=255)
#     upload_date = models.DateTimeField(auto_now_add=True)
#     # Add more fields as needed

#     def __str__(self):
#         return self.name

