# Generated by Django 3.1.5 on 2021-01-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(default=models.CharField(max_length=100), max_length=100),
        ),
    ]