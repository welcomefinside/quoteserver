from uuid import uuid4

from django.db import models

from .constants import QUOTE_STATUS_CHOICES


class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(blank=True, auto_now_add=True)
    modified = models.DateTimeField(blank=True, db_index=True)

    class Meta:
        abstract = True


class Quote(BaseModel):
    reference = models.CharField(max_length=12, blank=True)
    status = models.CharField(choices=QUOTE_STATUS_CHOICES, max_length=8)
    items = models.ManyToManyField(to="Item", null=True)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=10, default=None)
    notes = models.TextField(blank=True)
    company = models.ForeignKey(to="Company", on_delete=models.SET_NULL, null=True)


class Item(BaseModel):
    name = models.CharField(max_length=32, blank=True)
    description = models.TextField(blank=True)


class Company(BaseModel):
    name = models.CharField(db_index=True, max_length=256, blank=True)
    code = models.CharField(db_index=True, max_length=12, blank=True)
    acn = models.CharField("ACN", null=False, max_length=32, blank=True)
    abn = models.CharField("ABN", null=False, max_length=32, blank=True)
    app_token = models.UUIDField(default=uuid4, null=False, db_index=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Customer(BaseModel):
    name = models.CharField(db_index=True, max_length=256, blank=True)
    email = models.EmailField(db_index=True, blank=True)
    phone_number = models.CharField(db_index=True, max_length=16, blank=True)
    address = models.CharField(db_index=True, max_length=2056, blank=True)
