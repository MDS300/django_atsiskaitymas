# Generated by Django 4.1.2 on 2022-10-18 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projektai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saskaita',
            name='darbas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projektai.darbas'),
        ),
        migrations.AlterField(
            model_name='projektas',
            name='pabaigos_data',
            field=models.DateField(max_length=20, verbose_name='Pabaigos data'),
        ),
        migrations.AlterField(
            model_name='projektas',
            name='pradzios_data',
            field=models.DateField(max_length=20, verbose_name='Pradžios data'),
        ),
    ]
