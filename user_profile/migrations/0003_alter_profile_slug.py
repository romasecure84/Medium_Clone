# Generated by Django 5.0.2 on 2024-02-26 18:08

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0002_profile_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                unique_with=["user__first_name", "user__last_name"]
            ),
        ),
    ]