from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyAccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = MyAccountManager()

    def __str__(self):
        return self.username

class ChatHistory(models.Model):
    session_key = models.CharField(max_length=40)
    message = models.TextField()
    sender = models.CharField(max_length=10, choices=[('user', 'User'), ('bot', 'Bot')])
    created_at = models.DateTimeField(auto_now_add=True)
    attributes = models.JSONField(default=dict)

    def __str__(self):
        return f"ChatHistory {self.id} - {self.session_key} - {self.sender} - {self.created_at}"

class Feedback(models.Model):
    bot_message = models.TextField()
    feedback = models.TextField(blank=True, null=True)
    feedback_type = models.CharField(max_length=10, choices=[('positive', 'Positive'), ('negative', 'Negative')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id} - {self.feedback_type} - {self.created_at}"


from django.utils import timezone

class APICallCount(models.Model):
    function_name = models.CharField(max_length=255)  # Name of the function being tracked
    count = models.IntegerField(default=0)           # Count of how many times the function is called
    last_called = models.DateTimeField(auto_now=True) # Timestamp of the last function call

    def __str__(self):
        return f"{self.function_name}: {self.count} calls"



class ButtonClick(models.Model):
    count = models.IntegerField(default=0)
    def __str__(self):
        return f"Button clicked {self.count} times"
