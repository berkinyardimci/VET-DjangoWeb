# Generated by Django 4.0.2 on 2022-02-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='genus',
        ),
        migrations.AddField(
            model_name='animal',
            name='genus',
            field=models.ManyToManyField(blank=True, null=True, to='animals.Genus'),
        ),
    ]
