# Generated by Django 4.2.4 on 2023-08-15 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urldetail',
            old_name='user_id',
            new_name='user',
        ),
    ]
