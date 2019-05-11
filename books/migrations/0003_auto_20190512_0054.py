# Generated by Django 2.2.1 on 2019-05-11 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190512_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_categories',
            field=models.ManyToManyField(blank=True, null=True, to='books.BookCategory'),
        ),
        migrations.AlterField(
            model_name='book',
            name='library_branch',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.LibraryBranch'),
        ),
    ]