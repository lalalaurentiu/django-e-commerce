from tkinter.tix import Balloon
from django.db import models 

# change 
# from django.utils.translation import ugettext as _ 
# whith
# from django.utils.translation import gettext_lazy as _
# in 
# C:\Users\username\Desktop\Programare\e-commerce\e-commerce-env\Lib\site-packages\ fontawesome_5\ fields.py
from fontawesome_5.fields import IconField

class Category(models.Model):
    title = models.TextField(max_length=100)
    image = IconField()
    svg = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title