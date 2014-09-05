# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoteConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_name', models.CharField(default=b'4th IDEA Challenge', help_text=b'Vote title', max_length=255)),
                ('max_vote_per_user', models.IntegerField(default=3, help_text=b'Max votes a user can submit')),
                ('candidate_number', models.IntegerField(default=10, help_text=b'How many candidate do we have?')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidate', models.IntegerField(db_index=True)),
                ('count', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
