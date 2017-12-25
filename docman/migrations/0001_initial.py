# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 10, 9, 22, 16, 46, 449160, tzinfo=utc))),
                ('last_modified', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 10, 9, 22, 16, 46, 448658, tzinfo=utc))),
                ('last_modified', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(null=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 10, 9, 22, 16, 46, 451331, tzinfo=utc))),
                ('last_modified', models.DateTimeField(null=True)),
                ('access_type', models.ForeignKey(to='docman.AccessType')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 10, 9, 22, 16, 46, 449752, tzinfo=utc))),
                ('last_modified', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 10, 9, 22, 16, 46, 447731, tzinfo=utc))),
                ('last_modified', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=40, null=True)),
                ('lastname', models.CharField(max_length=40, null=True)),
                ('username', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 10, 9, 22, 16, 46, 450563, tzinfo=utc))),
                ('last_modified', models.DateTimeField(null=True)),
                ('department', models.ForeignKey(to='docman.Department')),
                ('role', models.ForeignKey(to='docman.Role')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='document_type',
            field=models.ForeignKey(to='docman.DocumentType'),
        ),
        migrations.AddField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(to='docman.Users'),
        ),
    ]
