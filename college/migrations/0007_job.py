# Generated by Django 4.0.4 on 2022-05-13 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_designation', models.CharField(default='', max_length=100)),
                ('no_of_seats', models.IntegerField(default=0)),
                ('last_date_to_apply', models.DateField(default=django.utils.timezone.now)),
                ('posted_date', models.DateField(default=django.utils.timezone.now)),
                ('relpy_email', models.EmailField(default='', max_length=55)),
            ],
        ),
    ]
