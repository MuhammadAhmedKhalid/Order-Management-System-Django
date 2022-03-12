# Generated by Django 3.0.8 on 2022-02-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('pro_quantity', models.IntegerField(default=0)),
                ('pro_price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='static/user/media/')),
            ],
        ),
    ]
