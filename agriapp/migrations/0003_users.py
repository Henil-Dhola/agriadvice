# Generated by Django 5.0.2 on 2024-09-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agriapp', '0002_remove_crops_id_alter_crops_name_requirements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
            ],
        ),
    ]