# Generated by Django 2.1.10 on 2019-07-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restobar', '0002_auto_20190702_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='pic',
            field=models.ImageField(default='', upload_to='resobar/static/images'),
        ),
    ]
