# Generated by Django 4.1.1 on 2023-05-28 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0019_rename_autobiographys_autobiography_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Licence",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="title")),
                ("content", models.TextField(max_length=10000, verbose_name="content")),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Licence1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="title")),
                ("content", models.TextField(max_length=10000, verbose_name="content")),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
            ],
        ),
    ]
