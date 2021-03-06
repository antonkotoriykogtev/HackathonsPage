# Generated by Django 3.0.4 on 2020-03-28 13:40

import datetime
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('reg', '0006_auto_20200325_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzer',
            name='place',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='uzer',
            name='school',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='uzer',
            name='skills',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='uzer',
            name='uni',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='uzer',
            name='uniEnd',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='uzer',
            name='age',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
