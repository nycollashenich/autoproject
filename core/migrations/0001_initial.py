# Generated by Django 5.0.6 on 2024-07-08 19:49

import core.models
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('modicado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('name_project', models.CharField(max_length=100, verbose_name='Name Project')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('coordinate', models.DecimalField(decimal_places=5, max_digits=5, verbose_name='Coordinates')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Latitude')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Longitude')),
                ('altitudealti', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Altutudealti')),
                ('point_x', models.FloatField()),
                ('point_y', models.FloatField()),
                ('point_z', models.FloatField()),
                ('altitudes_elavation', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Altitudes and elevation')),
                ('accountable', models.CharField(max_length=100, verbose_name='Accountable')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thum': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Image')),
                ('status', models.CharField(choices=[('in_progress', 'In progress'), ('finished', 'Finished'), ('canceled', 'Canceled')], max_length=20)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
