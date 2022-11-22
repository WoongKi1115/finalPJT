# Generated by Django 3.2.13 on 2022-11-22 11:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rates', models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(5)])),
                ('movie_comment', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
