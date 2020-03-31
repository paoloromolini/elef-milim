# Generated by Django 3.0.4 on 2020-03-31 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('lesson_link', models.URLField(blank=True, null=True)),
                ('audio_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('correct_answers', models.CharField(help_text='List separated by comma', max_length=250)),
                ('css_class', models.CharField(blank=True, max_length=250, null=True)),
                ('position', models.CharField(blank=True, max_length=250, null=True)),
                ('gender', models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female')], max_length=1, null=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Lesson')),
            ],
        ),
    ]