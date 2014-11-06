# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalDbModel',
            fields=[
                ('m_hk', models.IntegerField(serialize=False, primary_key=True)),
                ('m_kind', models.CharField(max_length=20)),
                ('m_ip', models.IPAddressField()),
                ('m_port', models.IntegerField(default=5432)),
                ('m_user', models.CharField(max_length=20)),
                ('m_pwd', models.CharField(max_length=20)),
                ('m_db', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'externaldb',
            },
            bases=(models.Model,),
        ),
    ]
