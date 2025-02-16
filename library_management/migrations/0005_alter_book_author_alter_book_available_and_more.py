# Generated by Django 5.0.3 on 2024-04-05 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0004_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.CharField(choices=[('T', 'TRUE'), ('F', 'FALSE')], max_length=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
