# Generated by Django 4.0.4 on 2022-08-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chiri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='carousel_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_img', models.ImageField(upload_to='carousel')),
            ],
        ),
    ]
