# Generated by Django 3.0.6 on 2020-06-01 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_at',
            field=models.DateTimeField(null=True),
        ),
    ]
