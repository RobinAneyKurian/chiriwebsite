# Generated by Django 4.0.4 on 2022-08-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chiri', '0002_carousel_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='carousel_images',
        ),
        migrations.AddField(
            model_name='logo',
            name='carousel_img',
            field=models.ImageField(null=True, upload_to='carousel'),
        ),
    ]
