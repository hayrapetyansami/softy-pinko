# Generated by Django 5.0.6 on 2024-06-22 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footertext',
            name='dynamic_text',
        ),
        migrations.DeleteModel(
            name='HeaderText',
        ),
        migrations.DeleteModel(
            name='DynamicText',
        ),
        migrations.DeleteModel(
            name='FooterText',
        ),
    ]
