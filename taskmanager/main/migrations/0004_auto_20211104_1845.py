# Generated by Django 3.2.5 on 2021-11-04 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211104_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='orders',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Cart', 'verbose_name_plural': 'Carts'},
        ),
        migrations.RemoveField(
            model_name='cart',
            name='final_price',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='for_anonymous_user',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='in_order',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total_products',
        ),
        migrations.AddField(
            model_name='cart',
            name='cover',
            field=models.ImageField(blank=True, default=True, upload_to='templates/photo'),
        ),
        migrations.AddField(
            model_name='cart',
            name='kolichestvo',
            field=models.IntegerField(default=True, verbose_name='koli'),
        ),
        migrations.AddField(
            model_name='cart',
            name='manga',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.IntegerField(default=True, verbose_name='Цена'),
        ),
        migrations.DeleteModel(
            name='CartProduct',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]