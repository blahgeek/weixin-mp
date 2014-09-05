# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotedUserModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(max_length=1024, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='voteconfiguration',
            name='dup_msg',
            field=models.CharField(default='\u6295\u7968\u5931\u8d25\uff01\u60a8\u5df2\u6295\u8fc7\uff01', help_text=b'Fail message for duplicate', max_length=1024),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='voteconfiguration',
            name='fail_msg',
            field=models.CharField(default='\u6295\u7968\u5931\u8d25\uff01\u6295\u7968\u683c\u5f0f\uff1a\u201c\u6295\u7968 3 4 5\u201d\uff0c\u6700\u591a\u53ef\u62953\u4e2a\u4e0d\u540c\u7684\u4f5c\u54c1\uff0c\u4f5c\u54c1\u8303\u56f4\u4e3a1-10', help_text=b'Fail message', max_length=1024),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='voteconfiguration',
            name='ok_msg',
            field=models.CharField(default='\u6295\u7968\u6210\u529f\uff01', help_text=b'Success message', max_length=1024),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='voteconfiguration',
            name='prefix',
            field=models.CharField(default='\u6295\u7968', help_text=b'Prefix for votes for detecting', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='votemodel',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
