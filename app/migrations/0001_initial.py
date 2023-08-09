# Generated by Django 3.2.15 on 2023-08-09 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_link', models.CharField(max_length=50, verbose_name='короткая ссылка')),
                ('full_link', models.TextField(verbose_name='длинная ссылка')),
                ('clicks_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='количество кликов')),
            ],
            options={
                'verbose_name': 'ссылка',
                'verbose_name_plural': 'ссылки',
                'db_table': 'links',
            },
        ),
    ]