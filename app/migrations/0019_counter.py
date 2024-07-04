# Generated by Django 5.0.6 on 2024-07-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_headertext_options_alter_reviews_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects', models.IntegerField(default=0)),
                ('happy_clients', models.IntegerField(default=0)),
                ('award_wins', models.IntegerField(default=0)),
                ('countries', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Counter',
                'verbose_name_plural': 'Counters',
            },
        ),
    ]
