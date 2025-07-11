# Generated by Django 5.0.6 on 2024-08-08 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_alter_fooddb_description_alter_fooddb_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddb',
            name='DESCRIPTION',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='fooddb',
            name='IMAGE',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]
