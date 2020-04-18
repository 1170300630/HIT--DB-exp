# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad_details',
            fields=[
                ('Advertisement_id', models.IntegerField(primary_key=True, serialize=False)),
                ('News_Title', models.CharField(primary_key=True, max_length=255)),
                ('Start_time', models.DateField(blank=True, null=True)),
                ('End_time', models.DateField(blank=True, null=True)),
                ('Pay', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Ad_details',
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('Advertisement_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Advertisement',
            },
        ),
        migrations.CreateModel(
            name='Branch_Office',
            fields=[
                ('Branch_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255, blank=True, null=True)),
                ('Address', models.CharField(max_length=255, blank=True, null=True)),
                ('Tel', models.IntegerField()),
            ],
            options={
                'db_table': 'Branch_Office',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Tel', models.IntegerField()),
                ('Rooms_no', models.IntegerField(blank=True, null=True)),
                ('Idel_rent', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Enterprise_owner',
            fields=[
                ('Owner_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255, blank=True, null=True)),
                ('Company_type', models.CharField(max_length=255, blank=True, null=True)),
                ('Tel', models.IntegerField()),
            ],
            options={
                'db_table': 'Enterprise_owner',
            },
        ),
        migrations.CreateModel(
            name='House_property',
            fields=[
                ('House_property_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Rooms_no', models.IntegerField(blank=True, null=True)),
                ('Address', models.CharField(max_length=255, blank=True, null=True)),
                ('Rent', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'House_property',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('Title', models.CharField(primary_key=True, max_length=255, serialize=False)),
                ('Address', models.CharField(max_length=255)),
                ('Tel', models.IntegerField()),
            ],
            options={
                'db_table': 'News',
            },
        ),
        migrations.CreateModel(
            name='Private_owener',
            fields=[
                ('Owner_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Tel', models.IntegerField()),
                ('Address', models.CharField(max_length=255, blank=True, null=True)),
            ],
            options={
                'db_table': 'Private_owener',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('Staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Customer_id', models.IntegerField(primary_key=True)),
                ('House_property_id', models.IntegerField(primary_key=True)),
                ('Timing', models.DateField(primary_key=True)),
                ('Comments', models.CharField(max_length=1023)),
            ],
            options={
                'db_table': 'Record',
            },
        ),
        migrations.CreateModel(
            name='Rent_contract',
            fields=[
                ('Contract_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Start_time', models.DateField(blank=True, null=True)),
                ('End_time', models.DateField(blank=True, null=True)),
                ('Rent', models.FloatField(blank=True, null=True)),
                ('Earnest_money', models.IntegerField(blank=True, null=True)),
                ('Customer', models.ForeignKey(to='rent_company.Customer')),
                ('House_property', models.ForeignKey(to='rent_company.House_property')),
            ],
            options={
                'db_table': 'Rent_contract',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('Staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=8)),
                ('Positions', models.CharField(max_length=255)),
                ('Salary', models.FloatField(blank=True, null=True)),
                ('Branch', models.ForeignKey(to='rent_company.Branch_Office')),
            ],
            options={
                'db_table': 'Staff',
            },
        ),
        migrations.AddField(
            model_name='rent_contract',
            name='Staff',
            field=models.ForeignKey(to='rent_company.Staff'),
        ),
        migrations.AlterUniqueTogether(
            name='record',
            unique_together=set([('Staff_id', 'Customer_id', 'House_property_id', 'Timing')]),
        ),
        migrations.AddField(
            model_name='house_property',
            name='Owner',
            field=models.ForeignKey(to='rent_company.Private_owener'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='House_property',
            field=models.ForeignKey(to='rent_company.House_property'),
        ),
        migrations.AlterUniqueTogether(
            name='ad_details',
            unique_together=set([('Advertisement_id', 'News_Title')]),
        ),
        migrations.AlterUniqueTogether(
            name='rent_contract',
            unique_together=set([('Contract_id', 'Customer', 'House_property', 'Staff')]),
        ),
    ]
