# Generated by Django 5.0.6 on 2024-06-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0007_remove_footertext_dynamic_text_delete_headertext_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Footer Text',
                'verbose_name_plural': 'Footer Text',
            },
        ),
        migrations.CreateModel(
            name='HeaderText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'Header Text',
                'verbose_name_plural': 'Header Text',
            },
        ),
        migrations.CreateModel(
            name='TreeBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='media/tree-blocks')),
            ],
            options={
                'verbose_name': 'Tree Block',
                'verbose_name_plural': 'Tree Blocks',
            },
        ),
    ]
