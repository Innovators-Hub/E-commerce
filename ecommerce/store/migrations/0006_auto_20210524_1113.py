# Generated by Django 3.1.3 on 2021-05-24 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_localproduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LocalProduct',
            new_name='Local',
        ),
    ]
