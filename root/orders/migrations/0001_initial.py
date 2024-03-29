# Generated by Django 4.2.4 on 2023-08-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name="Ім'я")),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='Телефон')),
                ('subject', models.TextField(max_length=256, verbose_name='Тема')),
                ('message', models.TextField(max_length=1024, verbose_name='Повідомлення')),
            ],
        ),
    ]
