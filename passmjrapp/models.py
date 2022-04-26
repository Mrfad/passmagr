from django.db import models
from django.contrib.auth.models import User

class PasswordGroup(models.Model):
    name = models.CharField(max_length=45, blank=True, default=None, null=True)
    
    def __str__(self):
        return self.name
    
class PasswordAccount(models.Model):
    group = models.ForeignKey(PasswordGroup, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, default=None, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    username_id = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=45, blank=True, null=True)
    rim = models.CharField(max_length=45, blank=True, null=True)
    subscription_number = models.CharField(max_length=45, blank=True, null=True)
    otp = models.CharField(max_length=45, blank=True, null=True)
    additional_notes = models.TextField(blank=True,default=None, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    user = models.ForeignKey(User,default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


