# Generated by Django 5.0.6 on 2024-07-04 11:48

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_pricingplan_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingPlanCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app.pricingplancategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='PricingPlan',
        ),
        migrations.DeleteModel(
            name='PricingPlanMain',
        ),
    ]
