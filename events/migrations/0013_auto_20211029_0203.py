# Generated by Django 2.2.13 on 2021-10-28 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20211028_2347'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EventJobCategoryLinking',
        ),
        migrations.DeleteModel(
            name='JobCategory',
        ),
    ]
