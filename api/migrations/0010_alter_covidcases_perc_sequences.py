# Generated by Django 4.0.2 on 2022-03-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_covidcases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidcases',
            name='perc_sequences',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]