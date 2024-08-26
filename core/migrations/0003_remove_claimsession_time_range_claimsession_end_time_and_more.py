# Generated by Django 4.2.14 on 2024-08-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_claim_claimsession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claimsession',
            name='time_range',
        ),
        migrations.AddField(
            model_name='claimsession',
            name='end_time',
            field=models.CharField(default='00:00', max_length=50),
        ),
        migrations.AddField(
            model_name='claimsession',
            name='start_time',
            field=models.CharField(default='00:00', max_length=50),
        ),
    ]
