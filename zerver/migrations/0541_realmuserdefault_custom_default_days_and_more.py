# Generated by Django 5.0.6 on 2024-06-23 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0540_remove_realm_create_private_stream_policy"),
    ]

    operations = [
        migrations.AddField(
            model_name="realmuserdefault",
            name="custom_default_days",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="realmuserdefault",
            name="custom_default_hours",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="custom_default_days",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="custom_default_hours",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
