# Generated by Django 3.0.6 on 2020-06-07 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_askme_questioncategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at']},
        ),
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
