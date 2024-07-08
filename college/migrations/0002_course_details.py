# Generated by Django 4.0.4 on 2022-05-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Details',
            fields=[
                ('course_name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('duration', models.CharField(default='1Year', max_length=45)),
                ('fees', models.IntegerField(default=0)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
