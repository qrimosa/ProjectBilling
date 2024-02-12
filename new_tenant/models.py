from django.db import models

# Create your models here.
class Tenant(models.Model):
    complex = models.CharField(max_length = 255)
    number_contract = models.CharField(max_length = 255)
    start_contract = models.DateField()
    end_contract = models.DateField()
    date_contract = models.DateField()
    tenant_name = models.CharField(max_length = 255)
    owner_name = models.CharField(max_length = 255)
    tenant_r_s = models.CharField(max_length = 255)
    type_of_contract = models.CharField(max_length=255)
    tax_on_ad = models.CharField(max_length=255)
    in_work = models.CharField(max_length=255)
    close = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    number_contract_in_check = models.CharField(max_length=255)
    main_contract = models.CharField(max_length=255)
    main_lot = models.CharField(max_length=255)