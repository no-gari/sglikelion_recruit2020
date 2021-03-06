# Generated by Django 3.0.4 on 2020-03-06 03:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.TextField(default='')),
                ('q2', models.TextField(default='')),
                ('q3', models.TextField(default='')),
                ('q4', models.TextField(default='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('final', models.BooleanField(default=False)),
                ('author', models.CharField(max_length=30)),
            ],
        ),
    ]
