# Generated by Django 5.0.1 on 2024-01-19 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="moviedata",
            name="typ",
            field=models.CharField(default="Action", max_length=200),
        ),
    ]