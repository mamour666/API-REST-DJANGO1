# Generated by Django 2.2.1 on 2019-05-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190530_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='singleProductPrice',
            field=models.CharField(max_length=1000000000),
        ),
        migrations.AlterField(
            model_name='order',
            name='totalPrice',
            field=models.CharField(max_length=100000000),
        ),
    ]
