# Generated by Django 3.2.1 on 2021-05-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fcuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'fastcampus_fcuser',
            },
        ),
    ]