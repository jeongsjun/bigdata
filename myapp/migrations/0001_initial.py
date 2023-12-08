# Generated by Django 4.2.7 on 2023-11-28 05:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Crawling14000",
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
                ("category", models.TextField(blank=True, null=True)),
                ("title", models.TextField(blank=True, null=True)),
                ("link", models.TextField(blank=True, null=True)),
                ("author", models.TextField(blank=True, null=True)),
                ("subtopic", models.TextField(blank=True, null=True)),
                ("content", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "main_crawling_14000",
            },
        ),
        migrations.CreateModel(
            name="User_Table",
            fields=[
                (
                    "name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("username", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
                ("birthdate", models.DateField()),
            ],
            options={
                "db_table": "user_table",
            },
        ),
    ]
