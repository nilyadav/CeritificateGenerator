# Generated by Django 4.1.7 on 2023-02-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('optional_email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('signature', models.FileField(default='', unique=True, upload_to='shop')),
            ],
            options={
                'db_table': 'Trainer',
            },
        ),
    ]
