# Generated by Django 3.0.6 on 2020-06-23 00:04

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_auto_20200623_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=articles.models.image_article_path),
        ),
    ]
