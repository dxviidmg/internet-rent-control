# Generated by Django 3.2.14 on 2022-07-14 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='has_late_payments',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.IntegerField(choices=[(0, 'Sin iniciar'), (1, 'Activo'), (2, 'Suspención'), (3, 'Cancelación')], default=0),
        ),
    ]