# Generated by Django 2.1.5 on 2019-02-09 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=30)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='UserDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=30, null=True)),
                ('last', models.CharField(default=None, max_length=30, null=True)),
                ('age', models.PositiveSmallIntegerField(default=None, null=True)),
                ('email', models.CharField(default=None, max_length=30, null=True)),
                ('role', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='authapp.RoleModel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userid', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userdata',
            },
        ),
    ]
