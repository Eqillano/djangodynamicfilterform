# Generated by Django 2.2.3 on 2020-06-26 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='journal',
            old_name='publish_data',
            new_name='publish_date',
        ),
    ]
