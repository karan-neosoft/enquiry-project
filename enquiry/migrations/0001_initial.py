# Generated by Django 2.0 on 2019-08-08 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50)),
                ('service', models.CharField(max_length=30)),
                ('budget', models.IntegerField()),
                ('message', models.CharField(max_length=450)),
            ],
            options={
                'db_table': 'enquiry_form',
                'managed': False,
            },
        ),
    ]