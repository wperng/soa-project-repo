from django.db import models

class Bookmark(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=True)
    hyperlink = models.CharField(max_length=500, null=False)
    created_date = models.DateTimeField(auto_now=True, null=True)
    owned_by = models.CharField(max_length=100, null=False)
    created_by = models.CharField(max_length=100, null=False)
    note = models.CharField(max_length=100, null=False)
