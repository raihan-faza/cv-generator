# Generated by Django 5.0.3 on 2024-05-13 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("linkedin", models.CharField(default=None, max_length=200)),
                ("github", models.CharField(default=None, max_length=200)),
                ("description", models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Degree",
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
                ("institution_name", models.CharField(max_length=100)),
                ("enter", models.DateField()),
                ("graduate", models.DateField()),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="generator.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=100)),
                ("details", models.TextField(max_length=100)),
                ("github_link", models.CharField(default=None, max_length=500)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="generator.profile",
                    ),
                ),
            ],
        ),
    ]
