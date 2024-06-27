# Generated by Django 5.0.6 on 2024-06-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeftBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='left-block')),
            ],
            options={
                'verbose_name': 'Left Block',
                'verbose_name_plural': 'Left Block',
            },
        ),
        migrations.CreateModel(
            name='RightBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='right-block')),
            ],
            options={
                'verbose_name': 'Right Block',
                'verbose_name_plural': 'Right Block',
            },
        ),
        migrations.AlterField(
            model_name='treeblocks',
            name='image',
            field=models.ImageField(upload_to='tree-blocks'),
        ),
    ]
