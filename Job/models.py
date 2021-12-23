from django.db import models

class Location(models.Model):
    key = models.AutoField(primary_key=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    zipcode = models.CharField(max_length=5, blank=True, null=True)


class Expenses(models.Model):
    key = models.AutoField(primary_key=True)
    hotel = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    food = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    other = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

class Job(models.Model):
    invoice_number = models.PositiveIntegerField(primary_key=True)
    revenue = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    distance = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    receipt_date = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=150, blank=True, null=True)
    tax = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    expenses = models.ForeignKey(Expenses, on_delete=models.CASCADE, blank=True, null=True)
    start_loc = models.ForeignKey(Location, on_delete=models.RESTRICT, blank=True, null=True, related_name="start")
    pickup_loc = models.ForeignKey(Location, on_delete=models.RESTRICT, blank=True, null=True, related_name="pickup")
    dropoff_loc = models.ForeignKey(Location, on_delete=models.RESTRICT, blank=True, null=True, related_name="dropoff")

class textEditor(models.Model):
   title = models.CharField(max_length=20)
   content = models.TextField()

   def __str__(self):
       return str(self.title)