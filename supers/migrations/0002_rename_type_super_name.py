# Generated by Django 4.0.3 on 2022-03-18 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super',
            old_name='type',
            new_name='name',
        ),
    ]