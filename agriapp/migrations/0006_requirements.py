# Generated by Django 5.0.2 on 2024-09-27 03:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agriapp', '0005_delete_requirements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soil', models.TextField()),
                ('ph', models.TextField()),
                ('fertility', models.TextField()),
                ('temperature', models.CharField(max_length=255)),
                ('sunlight', models.CharField(max_length=255)),
                ('water', models.CharField(max_length=255)),
                ('fertilizers', models.TextField()),
                ('duration', models.TextField()),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agriapp.crops')),
            ],
        ),
    ]
