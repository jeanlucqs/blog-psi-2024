# Generated by Django 5.1 on 2024-09-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(upload_to='static/imgs_post'),
        ),
    ]
