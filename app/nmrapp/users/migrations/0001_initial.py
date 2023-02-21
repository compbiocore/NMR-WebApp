# Generated by Django 4.1.7 on 2023-02-14 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StorageInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('parameter_1', models.IntegerField()),
                ('parameter_2', models.IntegerField()),
                ('file_path', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'storage',
            },
        ),
    ]
