# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-07-23 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libs', '0005_auto_20200723_1532'),
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibsPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='libs_cms_integration_libspluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('acct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libs.t_case')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
