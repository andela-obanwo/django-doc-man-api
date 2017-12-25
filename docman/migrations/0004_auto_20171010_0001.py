# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docman', '0003_auto_20171009_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=40, null=True)),
                ('lastname', models.CharField(max_length=40, null=True)),
                ('username', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('department', models.ForeignKey(to='docman.Department')),
                ('role', models.ForeignKey(to='docman.Role')),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='department',
        ),
        migrations.RemoveField(
            model_name='users',
            name='role',
        ),
        migrations.AlterField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(to='docman.User'),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
