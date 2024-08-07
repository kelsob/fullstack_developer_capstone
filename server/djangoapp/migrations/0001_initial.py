# Generated by Django 5.0.7 on 2024-07-22 18:00

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                (
                    'id', models.BigAutoField(
                        auto_created=True, primary_key=True,
                        serialize=False, verbose_name='ID'
                    )
                ),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                (
                    'id', models.BigAutoField(
                        auto_created=True, primary_key=True,
                        serialize=False, verbose_name='ID'
                    )
                ),
                (
                    'cartype', models.CharField(
                        choices=[
                            ('SEDAN', 'Sedan'),
                            ('SUV', 'SUV'),
                            ('COUPE', 'Coupe'),
                            ('HATCHBACK', 'Hatchback'),
                            ('STATIONWAGON', 'Station Wagon'),
                            ('TRUCK', 'Truck'), ('VAN', 'Van'),
                            ('CONVERTIBLE', 'Convertible'),
                            ('CROSSOVER', 'Crossover')
                        ],
                        default='SEDAN', max_length=12
                    )
                ),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('dealerid', models.IntegerField()),
                (
                    'year', models.IntegerField(
                        default=2000,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(2025)
                        ]
                    )
                ),
                (
                    'carmake', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='djangoapp.carmake'
                    )
                ),
            ],
        ),
    ]
