# Generated by Django 2.0.3 on 2018-04-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180405_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='product',
            field=models.ForeignKey(null=True, on_delete='CASCADE', related_name='categories', to='shop.Product'),
        ),
    ]
