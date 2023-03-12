# Generated by Django 3.2.16 on 2023-03-12 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('intro', models.CharField(max_length=192, verbose_name='Краткое описание')),
                ('description', models.CharField(max_length=2000, verbose_name='Подробное описание')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_top_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего события')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='own_projects', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Статус проекта',
                'verbose_name_plural': 'Статусы проекта',
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип проекта',
                'verbose_name_plural': 'Типы проекта',
            },
        ),
        migrations.CreateModel(
            name='ProjectTypeProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='Проект')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='projects.projecttype', verbose_name='Тип проекта')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='projects.projectstatus', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='project',
            name='types',
            field=models.ManyToManyField(through='projects.ProjectTypeProject', to='projects.ProjectType', verbose_name='Типы проекта'),
        ),
        migrations.AddConstraint(
            model_name='projecttypeproject',
            constraint=models.UniqueConstraint(fields=('project', 'type'), name='unique_project_type'),
        ),
    ]
