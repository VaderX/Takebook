# Generated by Django 3.0.3 on 2020-08-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatarea', '0007_auto_20200816_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='mReceived',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='chat',
            name='mSent',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
