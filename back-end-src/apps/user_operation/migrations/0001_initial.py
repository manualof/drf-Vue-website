# Generated by Django 2.0 on 2017-12-06 11:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('cases', models.ForeignKey(help_text='案例id', on_delete=django.db.models.deletion.CASCADE, to='cases.Cases', verbose_name='案例')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
            },
        ),
    ]