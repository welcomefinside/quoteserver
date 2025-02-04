# Generated by Django 3.2.25 on 2024-07-21 04:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True)),
                ('name', models.CharField(blank=True, db_index=True, max_length=256)),
                ('code', models.CharField(blank=True, db_index=True, max_length=12)),
                ('acn', models.CharField(blank=True, max_length=32, verbose_name='ACN')),
                ('abn', models.CharField(blank=True, max_length=32, verbose_name='ABN')),
                ('app_token', models.UUIDField(db_index=True, default=uuid.uuid4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True)),
                ('name', models.CharField(blank=True, max_length=32)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True)),
                ('reference', models.CharField(blank=True, max_length=12)),
                ('status', models.CharField(choices=[('quote', 'Quote'), ('deposit', 'Deposit'), ('paid', 'Paid')], max_length=8)),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('notes', models.TextField(blank=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quote.company')),
                ('items', models.ManyToManyField(null=True, to='quote.Item')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
