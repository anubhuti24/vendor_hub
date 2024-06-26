# Generated by Django 5.0.4 on 2024-05-01 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0008_delete_purchaseordermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrderModel',
            fields=[
                ('po_number', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('order_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')], default='PENDING', max_length=10)),
                ('quality_rating', models.FloatField()),
                ('issue_date', models.DateTimeField()),
                ('acknowledgment_date', models.DateTimeField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_order', to='vendor.vendorprofile')),
            ],
        ),
    ]
