# Generated by Django 3.1.7 on 2021-04-23 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_auto_20210419_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='naam', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mycart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpnigga', to='app.product'),
        ),
        migrations.AlterField(
            model_name='mycart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cnigga', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customerorder', to='app.customer'),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productorder', to='app.product'),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nigga', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clasr3', to='app.product'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alag', to=settings.AUTH_USER_MODEL),
        ),
    ]
