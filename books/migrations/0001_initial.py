# Generated by Django 2.2.1 on 2019-05-11 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pages_count', models.IntegerField()),
                ('publish_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hire_date', models.TimeField()),
                ('return_date', models.TimeField()),
                ('penalty_amount', models.IntegerField()),
                ('is_penalty', models.BooleanField(default=False)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('hired_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookAuthor', to='books.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_categories',
            field=models.ManyToManyField(to='books.BookCategory'),
        ),
        migrations.AddField(
            model_name='book',
            name='library_branch',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.LibraryBranch'),
        ),
    ]
