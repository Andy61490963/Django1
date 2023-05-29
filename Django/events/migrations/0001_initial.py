# Generated by Django 4.1.1 on 2022-09-19 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Interest",
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
                ("game", models.CharField(max_length=20, verbose_name="Interest Game")),
                ("code", models.CharField(max_length=20, verbose_name="Interest Code")),
                (
                    "Hobby",
                    models.CharField(max_length=20, verbose_name="Interest Hobby"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=20, verbose_name="Name")),
                (
                    "introduction",
                    models.TextField(max_length=500, verbose_name="Introduction"),
                ),
                (
                    "recent_events",
                    models.TextField(max_length=20, verbose_name="Recent_events"),
                ),
                ("event_date", models.DateTimeField(verbose_name="Event_date")),
                (
                    "autobiography",
                    models.TextField(max_length=500, verbose_name="Autobiography"),
                ),
                (
                    "interest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.interest",
                    ),
                ),
            ],
        ),
    ]
