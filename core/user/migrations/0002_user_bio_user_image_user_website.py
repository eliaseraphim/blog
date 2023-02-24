# Generated by Django 4.1.5 on 2023-01-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="bio",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="users/<django.db.models.fields.CharField>/%Y/%m/%d",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="website",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
