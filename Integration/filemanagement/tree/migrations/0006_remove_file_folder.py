# Generated by Django 2.0.3 on 2018-04-05 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0005_auto_20180401_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='folder',
        ),
    ]
