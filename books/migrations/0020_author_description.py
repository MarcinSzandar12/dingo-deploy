# Generated by Django 4.0.6 on 2022-09-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_author_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]