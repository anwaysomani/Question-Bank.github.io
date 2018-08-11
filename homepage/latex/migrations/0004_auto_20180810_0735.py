# Generated by Django 2.1 on 2018-08-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('latex', '0003_auto_20180808_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(blank=True, max_length=60)),
                ('course', models.CharField(blank=True, max_length=60)),
                ('module', models.IntegerField(blank=True)),
                ('chapter', models.IntegerField(blank=True)),
                ('question', models.CharField(blank=True, max_length=200)),
                ('marks', models.CharField(blank=True, choices=[(0, '2'), (1, '5'), (2, '10')], max_length=1)),
                ('priority', models.CharField(blank=True, choices=[(0, '1'), (1, '2'), (2, '3'), (3, '4')], max_length=1)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Question',
                'ordering': ('question',),
            },
        ),
        migrations.AlterIndexTogether(
            name='question',
            index_together={('branch', 'course', 'module', 'chapter', 'question', 'marks', 'priority')},
        ),
    ]