# Generated by Django 5.0.6 on 2024-07-13 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True, max_length=255)),
                ('html_class', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': ('Social',),
                'verbose_name_plural': 'Socials',
            },
        ),
    ]
