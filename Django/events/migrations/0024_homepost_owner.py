# Generated by Django 4.1.1 on 2023-05-29 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0023_information_ownerid"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepost",
            name="owner",
            field=models.IntegerField(default=1, verbose_name="Information Owner"),
        ),
    ]
