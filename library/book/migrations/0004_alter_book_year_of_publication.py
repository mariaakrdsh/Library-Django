# Generated by Django 4.1 on 2023-02-10 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_date_of_issue_book_year_of_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year_of_publication',
            field=models.IntegerField(blank=True, max_length=4),
        ),
    ]
