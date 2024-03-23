# Generated by Django 5.0.3 on 2024-03-15 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bin_data',
            fields=[
                ('bin_id', models.IntegerField(primary_key=True, serialize=False)),
                ('bin_code', models.CharField(max_length=12)),
                ('bin_country', models.CharField(max_length=100)),
                ('bin_brand', models.CharField(max_length=12)),
                ('bin_type', models.CharField(max_length=12)),
            ],
        ),
    ]
