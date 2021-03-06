# Generated by Django 2.2.5 on 2021-01-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coletor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=15)),
                ('place_id', models.IntegerField()),
                ('place_name', models.CharField(max_length=32)),
                ('battery', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('utcdate', models.DateTimeField()),
                ('connector_utcdate', models.DateTimeField()),
            ],
        ),
    ]
