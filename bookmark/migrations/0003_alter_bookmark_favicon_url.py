# Generated by Django 4.0 on 2022-09-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='favicon_url',
            field=models.URLField(blank=True),
        ),
    ]
