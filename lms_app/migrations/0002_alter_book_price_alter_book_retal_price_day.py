# Generated by Django 4.2.5 on 2023-10-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='retal_price_day',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]