# Generated by Django 5.1.4 on 2025-01-20 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicine_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('sale_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.customer')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.medicine')),
            ],
        ),
    ]
