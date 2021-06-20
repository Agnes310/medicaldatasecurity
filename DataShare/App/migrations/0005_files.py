# Generated by Django 2.0.12 on 2020-11-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_users_mob'),
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=200, unique=True)),
                ('desc', models.CharField(max_length=200, unique=True)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
    ]
