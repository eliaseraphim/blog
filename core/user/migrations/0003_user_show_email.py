# Generated by Django 4.1.5 on 2023-03-04 23:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_remove_user_show_email_user_show_website"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="show_email",
            field=models.BooleanField(
                default=False,
                help_text="Show email on personal page?",
                verbose_name="Show Email",
            ),
        ),
    ]
