# Generated by Django 3.2 on 2021-05-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='insurance_num',
            field=models.CharField(max_length=15),
        ),
    ]