# Generated by Django 4.1.7 on 2023-02-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usern', models.CharField(max_length=100, unique=True)),
                ('pword', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='storageinsert',
            name='file_path',
        ),
        migrations.RemoveField(
            model_name='storageinsert',
            name='parameter_1',
        ),
        migrations.RemoveField(
            model_name='storageinsert',
            name='parameter_2',
        ),
        migrations.AddField(
            model_name='storageinsert',
            name='folder',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='storageinsert',
            name='user_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='storageinsert',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='storageinsert',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterModelTable(
            name='storageinsert',
            table=None,
        ),
    ]
