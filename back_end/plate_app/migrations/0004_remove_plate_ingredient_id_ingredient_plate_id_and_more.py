# Generated by Django 4.2.4 on 2023-08-16 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0004_remove_journal_entry_plate_id'),
        ('plate_app', '0003_rename_unitname_measurement_unit_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plate',
            name='ingredient_id',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='plate_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='plates', to='plate_app.plate'),
        ),
        migrations.AddField(
            model_name='plate',
            name='journal_entry_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='plates', to='journal_app.journal_entry'),
        ),
    ]
