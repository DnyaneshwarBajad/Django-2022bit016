from django.db import models

class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()

