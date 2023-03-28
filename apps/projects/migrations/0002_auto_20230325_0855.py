# Generated by Django 3.2.16 on 2023-03-25 05:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='last_top_date',
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время удаления'),
        ),
        migrations.AddField(
            model_name='project',
            name='last_top_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='В топе последний раз'),
        ),
        migrations.AddField(
            model_name='projectstatus',
            name='order',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Порядок отображения'),
        ),
        migrations.AddField(
            model_name='projecttype',
            name='order',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Порядок отображения'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название'),
        ),
    ]
