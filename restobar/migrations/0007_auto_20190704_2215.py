# Generated by Django 2.1.10 on 2019-07-04 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restobar', '0006_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=200)),
                ('Pic', models.ImageField(default='', upload_to='images')),
                ('Description', models.TextField(default='')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='Name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_type',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='menu_item',
            name='MainMenuType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restobar.Menu'),
        ),
    ]
