from django.db import models

class Location(models.Model):
    key = models.AutoField(primary_key=True)
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=3, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)


class Expenses(models.Model):
    key = models.AutoField(primary_key=True)
    hotel = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    food = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    other = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

class Tafs(models.Model):
    invoice_number = models.CharField(max_length=12, primary_key=True)
    reference_number = models.CharField(max_length=12)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reserves = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    debtor = models.CharField(max_length=40, blank=True)

class Job(models.Model):
    comp_name = models.CharField(max_length=40, blank=True)
    rpm = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    distance = models.DecimalField(decimal_places=4, max_digits=9, blank=True, null=True)
    taf = models.ForeignKey(Tafs, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    receipt_date = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=250, blank=True, null=True)
    expenses = models.ForeignKey(Expenses, on_delete=models.CASCADE, blank=True, null=True)
    start_loc = models.ForeignKey(Location, on_delete=models.RESTRICT, blank=True, null=True, related_name="start")
    pickup_loc = models.ForeignKey(Location, on_delete=models.RESTRICT, blank=True, null=True, related_name="pickup")
    dropoff_loc = models.ForeignKey(Location, on_delete=models.RESTRICT, blank=True, null=True, related_name="dropoff")