# Generated by Django 3.1.7 on 2021-04-18 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210418_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_rate',
        ),
        migrations.AddField(
            model_name='rating',
            name='rate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
            preserve_default=False,
        ),
    ]
