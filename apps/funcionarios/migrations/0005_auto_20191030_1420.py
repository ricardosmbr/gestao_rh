# Generated by Django 2.1 on 2019-10-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0004_auto_20191030_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='departamento',
            field=models.ManyToManyField(to='departamentos.Departamento'),
        ),
    ]