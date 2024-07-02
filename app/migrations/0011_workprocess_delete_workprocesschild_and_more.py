# Generated by Django 5.0.6 on 2024-07-02 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_workprocessmain_workprocesschild'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='work-process')),
            ],
        ),
        migrations.DeleteModel(
            name='WorkProcessChild',
        ),
        migrations.DeleteModel(
            name='WorkProcessMain',
        ),
    ]
