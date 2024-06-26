# Generated by Django 4.1.7 on 2023-03-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]
