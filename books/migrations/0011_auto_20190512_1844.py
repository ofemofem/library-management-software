# Generated by Django 2.2.1 on 2019-05-12 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20190512_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
    ]
