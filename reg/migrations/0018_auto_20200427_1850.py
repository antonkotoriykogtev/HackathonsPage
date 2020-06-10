# Generated by Django 3.0.4 on 2020-04-27 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reg', '0017_auto_20200427_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsmodel',
            name='added_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
