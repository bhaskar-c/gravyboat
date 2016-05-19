# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gravyboat.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefit',
            name='proxy_class',
            field=gravyboat.models.fields.NullCharField(default=None, max_length=255, verbose_name='Custom class'),
            preserve_default=True,
        ),
    ]
