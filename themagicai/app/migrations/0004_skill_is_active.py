# Generated by Django 4.1.7 on 2023-02-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_letter_skills_alter_postcv_skills"),
    ]

    operations = [
        migrations.AddField(
            model_name="skill",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
