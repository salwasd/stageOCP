# Generated by Django 4.2.3 on 2023-08-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_stagiaire_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagiaire',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]