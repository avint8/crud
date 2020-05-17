from django.db import models


class table(models.Model):
    name    =    models.CharField(max_length=200)
    text    =    models.TextField()
    created =    models.DateTimeField(auto_now_add=True)
    edited  =    models.DateTimeField(auto_now=True)
