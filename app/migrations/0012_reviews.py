# Generated by Django 5.0.6 on 2024-07-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_workprocess_delete_workprocesschild_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=400)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('position', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='reviews')),
            ],
        ),
    ]
