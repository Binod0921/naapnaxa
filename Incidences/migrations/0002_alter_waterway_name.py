# Generated by Django 4.1.3 on 2022-12-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterway',
            name='name',
            field=models.CharField(max_length=48, null=True),
        ),
    ]
