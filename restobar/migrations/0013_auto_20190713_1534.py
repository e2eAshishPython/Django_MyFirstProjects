# Generated by Django 2.1.10 on 2019-07-13 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restobar', '0012_auto_20190713_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='reservations',
            name='preferred_food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Foods', to='restobar.Food_Type'),
        ),
    ]