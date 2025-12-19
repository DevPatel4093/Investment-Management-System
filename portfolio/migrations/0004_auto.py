from decimal import Decimal
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210128_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='current_price',
            field=models.DecimalField(decimal_places=5, default=Decimal('0'), max_digits=12),
        ),
    ]