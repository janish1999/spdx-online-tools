# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 09:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20170801_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConvertFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=16)),
                ('result', models.CharField(max_length=32)),
                ('file', models.FileField(upload_to=b'')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
