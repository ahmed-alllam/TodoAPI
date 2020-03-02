#   Copyright (c) Code Written and Tested by Ahmed Emad in 01/03/2020, 20:06
#

# Generated by Django 3.0.3 on 2020-03-01 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0004_auto_20200301_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos',
                                    to='core.TodoGroupModel'),
        ),
    ]