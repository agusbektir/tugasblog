# Generated by Django 3.0.6 on 2020-06-15 05:08

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20200607_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=articles.models.image_article_path),
        ),
    ]