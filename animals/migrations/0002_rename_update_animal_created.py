# Generated by Django 4.0.2 on 2022-02-11 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='update',
            new_name='created',
        ),
    ]
