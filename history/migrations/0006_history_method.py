# Generated by Django 3.1 on 2020-09-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0005_remove_history_object_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='method',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
