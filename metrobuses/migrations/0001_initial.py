# Generated by Django 4.0.3 on 2022-03-02 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alcaldias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metrobus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('metro_id', models.PositiveSmallIntegerField(unique=True)),
                ('alcaldia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alcaldias.alcaldia')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]