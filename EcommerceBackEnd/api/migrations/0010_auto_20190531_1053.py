# Generated by Django 2.2.1 on 2019-05-31 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190531_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='singleProductPrice',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='totalPrice',
            field=models.CharField(max_length=1000),
        ),
    ]
