# Generated by Django 2.1.1 on 2018-09-23 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_kot_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='kot',
            name='password',
            field=models.CharField(default='password', max_length=30),
        ),
    ]
