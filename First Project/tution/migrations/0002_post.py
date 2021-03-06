# Generated by Django 3.1.5 on 2021-01-26 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('salary', models.IntegerField()),
                ('details', models.TextField(max_length=600)),
                ('available', models.BooleanField()),
                ('category', models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
