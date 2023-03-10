# Generated by Django 4.1.2 on 2022-11-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('mobile', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=75, unique=True)),
                ('city', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
            ],
            options={
                'db_table': 'empdata',
            },
        ),
    ]
