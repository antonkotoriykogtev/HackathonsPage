# Generated by Django 3.0.4 on 2020-05-19 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0024_auto_20200510_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]
