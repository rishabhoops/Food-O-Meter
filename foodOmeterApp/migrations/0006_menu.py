# Generated by Django 4.2 on 2023-05-26 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodOmeterApp', '0005_alter_profile_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.CharField(max_length=50)),
                ('item_img', models.ImageField(upload_to='item_image')),
            ],
            options={
                'verbose_name_plural': 'Menu Table',
            },
        ),
    ]
