# Generated by Django 4.0.2 on 2022-03-05 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_date_consultaapi_data2_consultaapi_date1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultaapi',
            old_name='data2',
            new_name='date2',
        ),
    ]
