# Generated by Django 3.0 on 2023-02-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='scores',
            field=models.BigIntegerField(default=0),
        ),
    ]
