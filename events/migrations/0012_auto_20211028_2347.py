# Generated by Django 2.2.13 on 2021-10-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20211028_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoin',
            name='status',
            field=models.CharField(choices=[('Winner', 'Winner'), ('1st Runner up', '1st Runner Up'), ('2nd Runnerup', '2nd Runner Up')], max_length=20),
        ),
    ]
