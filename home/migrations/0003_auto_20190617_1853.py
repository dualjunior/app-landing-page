# Generated by Django 2.2.1 on 2019-06-17 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190617_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plusone',
            old_name='choise',
            new_name='choice',
        ),
    ]
