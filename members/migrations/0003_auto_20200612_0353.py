# Generated by Django 3.0.6 on 2020-06-12 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='media/'),
        ),
    ]
