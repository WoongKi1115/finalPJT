# Generated by Django 3.2.13 on 2022-11-16 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField()),
                ('backdrop_path', models.TextField()),
                ('original_language', models.CharField(max_length=50)),
                ('original_title', models.CharField(max_length=50)),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('poster_path', models.TextField()),
                ('release_date', models.DateField()),
                ('title', models.CharField(max_length=50)),
                ('video', models.BooleanField()),
                ('vote_average', models.FloatField()),
                ('vote_count', models.FloatField()),
                ('genre_ids', models.ManyToManyField(related_name='movies', to='movies.Genre')),
            ],
        ),
    ]