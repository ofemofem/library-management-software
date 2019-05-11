# Generated by Django 2.2.1 on 2019-05-11 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20190512_0122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookauthor',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.BookAuthor'),
        ),
    ]