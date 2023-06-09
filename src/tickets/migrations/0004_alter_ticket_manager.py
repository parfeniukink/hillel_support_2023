# Generated by Django 4.1.9 on 2023-06-15 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tickets", "0003_alter_ticket_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="manager",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="manager_tickets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
