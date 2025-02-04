# Generated by Django 5.1.1 on 2024-09-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('localtime', models.DateTimeField()),
                ('temp_c', models.FloatField()),
                ('temp_f', models.FloatField()),
                ('condition_text', models.CharField(max_length=100)),
                ('condition_code', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('wind_mph', models.FloatField()),
                ('wind_kph', models.FloatField()),
                ('pressure_mb', models.FloatField()),
                ('precip_mm', models.FloatField()),
                ('cloud', models.IntegerField()),
                ('feelslike_c', models.FloatField()),
                ('feelslike_f', models.FloatField()),
                ('uv', models.FloatField()),
            ],
        ),
    ]
