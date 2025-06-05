from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_remove_orderitem_order_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ] 