# Generated by Django 4.0.4 on 2022-05-27 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0009_consultancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('phone', models.CharField(max_length=10)),
                ('designation', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=45)),
                ('pic_name', models.FileField(default='', upload_to='college/picture')),
            ],
        ),
    ]
