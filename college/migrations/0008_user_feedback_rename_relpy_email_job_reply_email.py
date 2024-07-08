# Generated by Django 4.0.4 on 2022-05-16 07:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=45)),
                ('ratings', models.IntegerField(default=1)),
                ('review_text', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameField(
            model_name='job',
            old_name='relpy_email',
            new_name='reply_email',
        ),
    ]
