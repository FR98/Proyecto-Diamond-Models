# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 04:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('edad', models.IntegerField(default=0)),
                ('altura', models.FloatField(default=0.0)),
                ('peso', models.FloatField(default=0.0)),
                ('telefono', models.IntegerField(default=0)),
                ('correo', models.CharField(max_length=50)),
                ('agencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencias.Agencia')),
            ],
        ),
    ]
