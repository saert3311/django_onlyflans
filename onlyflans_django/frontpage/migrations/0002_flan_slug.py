# Generated by Django 4.2.11 on 2024-04-18 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='slug',
            field=models.SlugField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
