# Generated by Django 4.2.4 on 2023-12-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yes24', '0002_alter_yes24bestlist_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yes24bestlist',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]