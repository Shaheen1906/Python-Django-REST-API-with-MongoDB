# Generated by Django 3.2.13 on 2022-12-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRUD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('img', models.ImageField(upload_to='')),
                ('summary', models.CharField(max_length=500)),
            ],
        ),
    ]