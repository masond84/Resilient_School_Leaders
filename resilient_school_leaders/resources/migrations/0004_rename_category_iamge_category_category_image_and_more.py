# Generated by Django 4.2 on 2023-05-14 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_category_category_iamge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_iamge',
            new_name='category_image',
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=100),
        ),
    ]
