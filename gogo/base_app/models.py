import uuid
from django.db import models

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date", null=True)
    modified_date = models.DateTimeField(auto_now=True, verbose_name="Modified Date", null=True)

    class Meta:
        abstract = True


class ClientBaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="Modified Date")
    client_id = models.IntegerField(default=-1, verbose_name="Client id")
    client_code = models.CharField(max_length=128, verbose_name="Client Code")

    class Meta:
        abstract = True

