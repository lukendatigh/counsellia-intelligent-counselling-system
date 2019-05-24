# Generated by Django 2.1.4 on 2019-03-04 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellia', '0011_appointment_requested'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['counsellee', '-time']},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_type',
            field=models.CharField(choices=[('first', 'First appointment'), ('follow-up', 'Follow-up appointment'), ('final', 'Final appointment')], max_length=20, null=True, verbose_name='Appointment Type'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Short Description'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='sentiment',
            field=models.TextField(null=True, verbose_name='sentiment analysis'),
        ),
        migrations.AlterField(
            model_name='report',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='topic',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='word_count',
            field=models.TextField(blank=True, null=True),
        ),
    ]
