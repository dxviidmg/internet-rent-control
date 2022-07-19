# Generated by Django 3.2.14 on 2022-07-19 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_package_payment_frequency'),
        ('services', '0003_alter_service_start_date_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.package', verbose_name='Paquete'),
        ),
    ]
