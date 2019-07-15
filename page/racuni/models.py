from django.db import models
from django.contrib.postgres.fields import ArrayField


class SavedTemplate(models.Model):
    username = models.CharField(max_length=30, unique=True)

    comp_name = models.CharField(max_length=50)
    house_nr = models.CharField(max_length=30)
    post_nr = models.CharField(max_length=4)
    city = models.CharField(max_length=30)

    bill_city = models.CharField(max_length=30)
    tax_nr = models.CharField(max_length=20)
    id_nr = models.CharField(max_length=20)  # matična številka
    transact_acc = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    full_name = models.CharField(max_length=50)


class SavedReceipt(models.Model):
    username = models.CharField(max_length=30)

    comp_name = models.CharField(max_length=50)
    house_nr = models.CharField(max_length=30)
    post_nr = models.CharField(max_length=4)
    city = models.CharField(max_length=30)

    bill_city = models.CharField(max_length=30)
    date = models.DateField()
    tax_nr = models.CharField(max_length=20)
    id_nr = models.CharField(max_length=20)  # matična številka
    transact_acc = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    bill_number = models.CharField(max_length=20)
    buyer_full_name = models.CharField(max_length=50)
    buyer_house_nr = models.CharField(max_length=30)
    buyer_post_nr = models.CharField(max_length=4)
    id_for_vat = models.CharField(max_length=20)

    task_date = models.DateField()
    payment_date = models.DateField()

    task = models.CharField(max_length=50)

    # Table of tasks
    opravilo = ArrayField(models.CharField(max_length=50))
    measure_unit = ArrayField(models.CharField(max_length=10))
    cents_per_quantity = ArrayField(models.IntegerField())
    quantity = ArrayField(models.DecimalField(max_digits=10, decimal_places=4))

    full_name = models.CharField(max_length=50)
