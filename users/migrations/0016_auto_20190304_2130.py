# Generated by Django 2.1.4 on 2019-03-04 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20190225_0903'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='counselling',
            options={'ordering': ['-date_contacted'], 'verbose_name': 'Connection', 'verbose_name_plural': 'Connections'},
        ),
        migrations.AlterField(
            model_name='user',
            name='is_counsellee',
            field=models.BooleanField(default=False, null=True, verbose_name='counsellee status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_counsellor',
            field=models.BooleanField(default=False, null=True, verbose_name='counsellor status'),
        ),
    ]
