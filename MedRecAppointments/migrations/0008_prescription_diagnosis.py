# Generated by Django 3.1.7 on 2021-05-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('MedRecAppointments', '0007_auto_20210518_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='diagnosis',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]