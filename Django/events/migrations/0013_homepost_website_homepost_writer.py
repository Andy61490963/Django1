# Generated by Django 4.1.2 on 2022-10-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0012_homepost"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepost",
            name="website",
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="homepost",
            name="writer",
            field=models.CharField(max_length=20, null=True, verbose_name="Name"),
        ),
    ]
