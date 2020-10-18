# Generated by Django 3.0.3 on 2020-10-18 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=63, unique=True)),
                ('short_description', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DropdownField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('function', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('multiple_selection_allowed', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=63, unique=True)),
                ('display_name', models.CharField(max_length=63, unique=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('required', models.BooleanField(default=True)),
                ('entity_object_id', models.PositiveIntegerField()),
                ('entity_content_type', models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'pseudoc_framework'), ('model', 'textfield')), models.Q(('app_label', 'pseudoc_framework'), ('model', 'numericfield')), models.Q(('app_label', 'pseudoc_framework'), ('model', 'dropdownfield')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NumericField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('min', models.IntegerField(blank=True, null=True)),
                ('max', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('max_length', models.IntegerField(blank=True, default=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(max_length=63, unique=True)),
                ('short_description', models.CharField(blank=True, max_length=127, null=True)),
                ('api', models.URLField()),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queries', to='pseudoc_framework.App')),
                ('field_list', models.ManyToManyField(blank=True, related_name='field_query', to='pseudoc_framework.Field')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
