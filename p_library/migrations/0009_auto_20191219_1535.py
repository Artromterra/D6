# Generated by Django 2.2.6 on 2019-12-19 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0008_auto_20191218_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=20),
        ),
    ]
