from django.db import models
from django.contrib.auth.models import User



class PasswordAccount(models.Model):
    title = models.CharField(max_length=45, blank=True, default=None, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    additional_notes = models.TextField(blank=True,default=None, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(User,default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



