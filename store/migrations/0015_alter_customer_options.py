# Generated by Django 4.2.5 on 2024-05-06 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': [('view_history', 'Can view history')]},
        ),
    ]
