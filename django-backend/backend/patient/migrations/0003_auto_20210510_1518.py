# Generated by Django 3.2 on 2021-05-10 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_insurance_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drugs',
            name='dosage',
        ),
        migrations.RemoveField(
            model_name='drugs',
            name='form',
        ),
        migrations.RemoveField(
            model_name='drugs',
            name='strength',
        ),
    ]