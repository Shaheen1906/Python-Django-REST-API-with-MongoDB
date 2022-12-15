from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRUD',
            fields=[
                ('name', models.CharField(max_length=70, blank=False,)),
                ('img',models.ImageField()),
                ('summary', models.CharField(max_length=500, blank=False,)),
            ],
        ),
    ]