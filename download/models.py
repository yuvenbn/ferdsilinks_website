from django.db import models
from django.contrib.auth.models import User

class Download(models.Model):
    user_fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country= models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    download_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file_name} - {self.user_fullname}"