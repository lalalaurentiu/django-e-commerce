from distutils.command.upload import upload
from django.db import models

class Claim(models.Model):
    image = models.ImageField(upload_to = "images/Claim")
    title = models.TextField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title
