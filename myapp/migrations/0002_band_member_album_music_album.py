# Generated by Django 4.1 on 2023-03-02 16:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'band',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='myapp.band')),
            ],
            options={
                'db_table': 'member',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albuns', to='myapp.band')),
            ],
            options={
                'db_table': 'album',
            },
        ),
        migrations.AddField(
            model_name='music',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='myapp.album'),
            preserve_default=False,
        ),
    ]
