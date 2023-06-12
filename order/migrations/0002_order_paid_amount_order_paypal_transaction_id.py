# Generated by Django 4.1.1 on 2023-06-12 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='paypal_transaction_id',
            field=models.CharField(default='12345', max_length=30),
            preserve_default=False,
        ),
    ]
