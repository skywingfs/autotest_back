# Generated by Django 2.1.4 on 2020-08-12 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='post',
            new_name='position',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='menus',
        ),
        migrations.AddField(
            model_name='menu',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='显示标记'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='is_frame',
            field=models.BooleanField(default=False, verbose_name='外部菜单'),
        ),
    ]
