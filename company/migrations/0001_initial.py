# Generated by Django 4.1.4 on 2022-12-14 16:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'benefits',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('logo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('essentiality', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facilities', to='company.category')),
            ],
            options={
                'db_table': 'facilities',
            },
        ),
        migrations.CreateModel(
            name='CompanyBenefit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
                ('benefit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefits', to='company.benefit')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_benefits', to='company.company')),
            ],
            options={
                'db_table': 'company_benefits',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='benefits',
            field=models.ManyToManyField(related_name='companies', through='company.CompanyBenefit', to='company.benefit'),
        ),
        migrations.AddField(
            model_name='benefit',
            name='facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefits', to='company.facility'),
        ),
    ]
