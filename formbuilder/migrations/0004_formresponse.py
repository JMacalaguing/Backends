# Generated by Django 5.0.4 on 2024-11-29 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formbuilder', '0003_alter_form_schema'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_data', models.JSONField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_responses', to='formbuilder.form')),
            ],
        ),
    ]
