# Generated by Django 4.2.4 on 2023-08-23 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="authentication",
            old_name="title",
            new_name="phone",
        ),
    ]
