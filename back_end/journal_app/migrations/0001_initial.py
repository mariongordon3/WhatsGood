# Generated by Django 4.2.4 on 2023-08-11 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plate_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal_entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('plate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plates', to='plate_app.plate')),
            ],
        ),
    ]
