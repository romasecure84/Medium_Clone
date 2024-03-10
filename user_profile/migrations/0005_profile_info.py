# Generated by Django 5.0.2 on 2024-03-10 16:03

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0004_alter_profile_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="info",
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]