# Generated by Django 4.1.2 on 2022-10-27 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]