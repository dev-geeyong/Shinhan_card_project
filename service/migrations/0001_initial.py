# Generated by Django 2.2.4 on 2020-08-30 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CTY_NM_2', models.CharField(max_length=20)),
                ('USE_CUS_CNT', models.FloatField()),
                ('CORONA_CNT', models.FloatField()),
                ('CLEAN', models.FloatField()),
            ],
        ),
    ]
