# Generated by Django 4.2 on 2023-04-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='вопрос')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wording', models.CharField(max_length=255, verbose_name='формулировка')),
                ('date', models.DateField(verbose_name='дата')),
            ],
            options={
                'verbose_name': 'Решение',
                'verbose_name_plural': 'Решения',
            },
        ),
    ]