# Generated by Django 2.1.4 on 2019-02-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190205_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='counsellor',
            name='quote',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='counsellor',
            name='website',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
