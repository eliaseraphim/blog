# Generated by Django 4.1.5 on 2023-02-24 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                help_text="Author of the post.",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Image uploaded with post.",
                null=True,
                upload_to="images/%Y/%m/%d",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="text",
            field=models.TextField(help_text="Text of the post."),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(help_text="Title of the post.", max_length=200),
        ),
    ]
