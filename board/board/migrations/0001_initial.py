# Generated by Django 4.2.3 on 2023-07-27 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='수정날짜')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='수정날짜')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.question')),
            ],
        ),
    ]