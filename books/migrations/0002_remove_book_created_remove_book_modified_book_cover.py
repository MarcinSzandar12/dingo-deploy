# Generated by Django 4.0.6 on 2022-08-09 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='created',
        ),
        migrations.RemoveField(
            model_name='book',
            name='modified',
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.CharField(blank=True, choices=[('hard', 'Twarda okładka'), ('soft', 'Miękka okładka')], max_length=50, null=True),
        ),
    ]
