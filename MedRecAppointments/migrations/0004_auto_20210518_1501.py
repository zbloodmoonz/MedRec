# Generated by Django 3.1.7 on 2021-05-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('MedRecAppointments', '0003_patientcreation_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientcreation',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=20),
        ),
    ]
