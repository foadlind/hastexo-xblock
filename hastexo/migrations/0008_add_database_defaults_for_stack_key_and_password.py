# Generated by Django 2.2.19 on 2021-03-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hastexo', '0007_add_delete_by_and_delete_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stack',
            name='key',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='stack',
            name='password',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
