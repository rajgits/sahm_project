# Generated by Django 3.0.5 on 2020-04-26 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sahm_app', '0009_emails_manageposts_usercontact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emails',
            options={'managed': False, 'verbose_name_plural': 'Email Templates'},
        ),
        migrations.AlterModelOptions(
            name='manageposts',
            options={'managed': False, 'verbose_name_plural': 'Job Posts'},
        ),
        migrations.AlterModelOptions(
            name='usercontact',
            options={'managed': False, 'verbose_name_plural': 'Contact Queries'},
        ),
    ]