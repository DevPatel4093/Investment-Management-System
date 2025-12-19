from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_manual_20210126_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset',
            name='current_price',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]