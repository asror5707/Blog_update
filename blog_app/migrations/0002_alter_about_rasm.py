# Generated by Django 4.0.3 on 2022-04-22 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='rasm',
            field=models.FileField(blank=True, upload_to='static/media/'),
        ),
    ]
