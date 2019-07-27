from django.db import models
from django.contrib.postgres.fields import ArrayField


class SavedTemplate(models.Model):
    username = models.CharField(max_length=30, unique=True)

    comp_name = models.CharField(max_length=50, blank=True, null=True)
    house_nr = models.CharField(max_length=30, blank=True, null=True)
    post_nr = models.CharField(max_length=4, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)

    bill_city = models.CharField(max_length=30, blank=True, null=True)
    tax_nr = models.CharField(max_length=20, blank=True, null=True)
    id_nr = models.CharField(max_length=20, blank=True, null=True)  # matična številka
    transact_acc = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    full_name = models.CharField(max_length=50, blank=True, null=True)


class SavedReceipt(models.Model):
    username = models.CharField(max_length=30, blank=True, null=True)

    comp_name = models.CharField(max_length=50, blank=True, null=True)
    house_nr = models.CharField(max_length=30, blank=True, null=True)
    post_nr = models.CharField(max_length=4, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)

    bill_city = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    tax_nr = models.CharField(max_length=20, blank=True, null=True)
    id_nr = models.CharField(max_length=20, blank=True, null=True)  # matična številka
    transact_acc = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    bill_number = models.CharField(max_length=20, blank=True, null=True)
    buyer_full_name = models.CharField(max_length=50, blank=True, null=True)
    buyer_house_nr = models.CharField(max_length=30, blank=True, null=True)
    buyer_post_nr = models.CharField(max_length=4, blank=True, null=True)
    buyer_city = models.CharField(max_length=20, blank=True, null=True)
    id_for_vat = models.CharField(max_length=20, blank=True, null=True)

    task_date = models.DateField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)

    task = models.CharField(max_length=50, blank=True, null=True)

    # Table of tasks
    opravilo = ArrayField(models.CharField(max_length=50),
                          blank=True, null=True)
    measure_unit = ArrayField(models.CharField(max_length=10),
                              blank=True, null=True)
    cents_per_quantity = ArrayField(models.IntegerField(),
                                    blank=True, null=True)
    quantity = ArrayField(models.DecimalField
                          (max_digits=10, decimal_places=4),
                          blank=True, null=True)

    full_name = models.CharField(max_length=50, blank=True, null=True)
