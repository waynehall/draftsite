# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draftmain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_3PTPCT',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_ASTPCT',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_BLKPCT',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_DBPM',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_OBPM',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_PER',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_REBPCT',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_STLPCT',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_TS',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_WS48',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20),
        ),
    ]
