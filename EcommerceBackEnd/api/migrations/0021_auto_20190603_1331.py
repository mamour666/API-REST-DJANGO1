# Generated by Django 2.2.1 on 2019-06-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20190603_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='singleProductPrice',
        ),
        migrations.RemoveField(
            model_name='order',
            name='totalPrice',
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.TextField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='productName',
            field=models.CharField(max_length=1000000000000),
        ),
    ]
