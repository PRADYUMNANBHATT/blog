# Generated by Django 3.2.5 on 2021-07-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogspot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='portfolio/images/'),
        ),
    ]
