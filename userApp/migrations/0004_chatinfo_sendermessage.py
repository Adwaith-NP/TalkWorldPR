# Generated by Django 4.2.4 on 2023-11-04 09:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("userApp", "0003_remove_chatinfo_sendermessage"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatinfo",
            name="senderMessage",
            field=models.TextField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
