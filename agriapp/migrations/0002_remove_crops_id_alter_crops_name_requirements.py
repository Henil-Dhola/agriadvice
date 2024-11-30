# Generated by Django 5.0.2 on 2024-09-10 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agriapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crops',
            name='id',
        ),
        migrations.AlterField(
            model_name='crops',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fertilizers', models.TextField()),
                ('pesticides', models.TextField()),
                ('ph', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('waterIrrigation', models.CharField(max_length=255)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agriapp.crops')),
            ],
        ),
    ]