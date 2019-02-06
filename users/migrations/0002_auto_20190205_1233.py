# Generated by Django 2.1.4 on 2019-02-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counsellor',
            name='qualification',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='counsellee',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='counsellee',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='short bio'),
        ),
        migrations.AlterField(
            model_name='counsellee',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='counsellee',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='counsellee',
            name='interests',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='counsellee',
            name='phone_number',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='mobile number'),
        ),
        migrations.AlterField(
            model_name='counsellor',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='counsellor',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='short bio'),
        ),
        migrations.AlterField(
            model_name='counsellor',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='counsellor',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='counsellor',
            name='phone_number',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='mobile number'),
        ),
        migrations.AlterField(
            model_name='counsellor',
            name='website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
