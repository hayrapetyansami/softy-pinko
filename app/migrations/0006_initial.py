# Generated by Django 5.0.6 on 2024-06-22 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0005_remove_footertext_dynamic_text_delete_headertext_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('dynamic_text', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footer_texts', to='app.dynamictext')),
            ],
        ),
        migrations.CreateModel(
            name='HeaderText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('dynamic_text', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='header_texts', to='app.dynamictext')),
            ],
        ),
    ]
