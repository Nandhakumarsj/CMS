# Generated by Django 4.1 on 2024-02-24 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(blank=True, default='excelnandhu@gmail.com', max_length=54),
        ),
    ]
