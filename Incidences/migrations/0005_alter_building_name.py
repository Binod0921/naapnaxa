# Generated by Django 4.1.3 on 2022-12-08 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidences', '0004_alter_road_shape_len'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='name',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
