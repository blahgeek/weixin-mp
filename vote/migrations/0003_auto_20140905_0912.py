# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20140905_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voteconfiguration',
            name='dup_msg',
            field=models.TextField(default='\u6295\u7968\u5931\u8d25\uff01\u60a8\u5df2\u6295\u8fc7\uff01', help_text=b'Fail message for duplicate'),
        ),
        migrations.AlterField(
            model_name='voteconfiguration',
            name='fail_msg',
            field=models.TextField(default='\u6295\u7968\u5931\u8d25\uff01\u6295\u7968\u683c\u5f0f\uff1a\u201c\u6295\u7968 3 4 5\u201d\uff0c\u6700\u591a\u53ef\u62953\u4e2a\u4e0d\u540c\u7684\u4f5c\u54c1\uff0c\u4f5c\u54c1\u8303\u56f4\u4e3a1-10', help_text=b'Fail message'),
        ),
        migrations.AlterField(
            model_name='voteconfiguration',
            name='ok_msg',
            field=models.TextField(default='\u6295\u7968\u6210\u529f\uff01', help_text=b'Success message'),
        ),
    ]
