# Generated by Django 3.1 on 2020-08-28 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userloginactivity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLoginActivity',
        ),
    ]