# Generated by Django 4.2.3 on 2023-07-16 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='message',
            new_name='Subject',
        ),
    ]
