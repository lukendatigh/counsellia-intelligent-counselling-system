# Generated by Django 2.1.4 on 2019-03-20 22:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0017_auto_20190314_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counsellee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Counsellee')),
                ('counsellor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Counsellor')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('conversation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.Conversation')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
