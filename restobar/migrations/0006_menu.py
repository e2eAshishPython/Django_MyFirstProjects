# Generated by Django 2.1.10 on 2019-07-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restobar', '0005_auto_20190703_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='null', max_length=200)),
                ('menu_type', models.CharField(default='null', max_length=200)),
            ],
        ),
    ]
