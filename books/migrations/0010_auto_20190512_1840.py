# Generated by Django 2.2.1 on 2019-05-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20190512_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='hire_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='hire',
            name='return_date',
            field=models.DateTimeField(),
        ),
    ]