# Generated by Django 2.2.1 on 2019-05-13 23:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0005_auto_20190514_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 13, 1, 6, 16, 523882)),
        ),
    ]
