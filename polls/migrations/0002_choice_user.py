# Generated by Django 4.0.4 on 2022-05-03 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='user',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
