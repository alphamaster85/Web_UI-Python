# Generated by Django 2.1.5 on 2019-01-30 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_auto_20190130_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdatamodel',
            name='date',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='user',
        ),
        migrations.AddField(
            model_name='userdatamodel',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userid', to='formapp.UserModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='date',
            field=models.DateField(default=None),
        ),
    ]