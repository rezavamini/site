# Generated by Django 3.2.4 on 2023-08-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='blog/'),
        ),
    ]