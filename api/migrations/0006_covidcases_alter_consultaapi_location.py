# Generated by Django 4.0.2 on 2022-03-09 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_date1_consultaapi_datafinal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('variant', models.CharField(max_length=10)),
                ('num_sequences', models.IntegerField(max_length=100)),
                ('perc_sequences', models.IntegerField(max_length=100)),
                ('num_sequences_total', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='consultaapi',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
