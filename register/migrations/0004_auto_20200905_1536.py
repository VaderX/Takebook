# Generated by Django 3.0.3 on 2020-09-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20200905_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mImage',
            field=models.TextField(default='../../../register/static/register/images/user.png'),
        ),
    ]
