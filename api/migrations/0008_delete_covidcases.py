# Generated by Django 4.0.2 on 2022-03-10 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_covidcases_num_sequences_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CovidCases',
        ),
    ]
