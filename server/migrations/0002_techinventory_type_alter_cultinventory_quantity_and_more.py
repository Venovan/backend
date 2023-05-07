# Generated by Django 4.1.3 on 2023-04-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='techinventory',
            name='type',
            field=models.CharField(choices=[('E', 'Electrical'), ('M', 'Mechanical')], default='E', max_length=20),
        ),
        migrations.AlterField(
            model_name='cultinventory',
            name='quantity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sportinventory',
            name='quantity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='techinventory',
            name='quantity',
            field=models.FloatField(),
        ),
    ]