# Generated by Django 2.1.10 on 2019-07-08 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restobar', '0008_auto_20190704_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu_item',
            name='MainMenuType',
        ),
        migrations.AddField(
            model_name='menu_item',
            name='MainMenuType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restobar.Menu'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='Name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
