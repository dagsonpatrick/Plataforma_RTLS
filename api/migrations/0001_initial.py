# Generated by Django 2.2.5 on 2021-01-09 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collaborator', '0001_initial'),
        ('tag', '0001_initial'),
        ('anchor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=15)),
                ('place_id', models.IntegerField()),
                ('place_name', models.CharField(max_length=32)),
                ('utcdate', models.DateTimeField()),
                ('connector_utcdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EventoDevAWS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('place_name', models.CharField(max_length=32)),
                ('distance', models.IntegerField()),
                ('last_seen', models.DateTimeField()),
                ('utcdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='InfoEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_tag', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('foto', models.CharField(max_length=100)),
                ('permanencia', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='InfoPlanta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_plano', models.IntegerField(blank=True, null=True)),
                ('name_plano', models.CharField(max_length=50)),
                ('description_plano', models.CharField(max_length=50)),
                ('foto_plano', models.CharField(max_length=100)),
                ('qtd_colaborador', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtInicio', models.DateTimeField()),
                ('dtFim', models.DateTimeField(blank=True, null=True)),
                ('permanencia', models.TimeField(blank=True, null=True)),
                ('status', models.IntegerField()),
                ('idanchor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anchor.Anchor')),
                ('idcolaborador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collaborator.Collaborator')),
                ('idtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.Tag')),
            ],
        ),
    ]