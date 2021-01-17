# Generated by Django 3.1.5 on 2021-01-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('available_quantity', models.IntegerField(default=0)),
                ('discounts', models.CharField(choices=[('a', '50% discount'), ('b', '1 free for 2'), ('c', 'No discount')], default='c', max_length=30)),
            ],
        ),
    ]
