# Generated by Django 5.0.2 on 2024-02-25 17:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Film', 'verbose_name_plural': 'Filmler'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Kişi', 'verbose_name_plural': 'Kişiler'},
        ),
        migrations.AddField(
            model_name='movie',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateField(verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(20)], verbose_name='Özet'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image_name',
            field=models.CharField(max_length=50, verbose_name='Resim'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='person',
            name='duty_type',
            field=models.CharField(choices=[('1', 'Görevli'), ('2', 'Oyuncu'), ('3', 'Yönetmen'), ('4', 'Senarist')], max_length=1, verbose_name='Görev'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('M', 'Erkek'), ('F', 'Kadın')], max_length=1, verbose_name='Cinsiyet'),
        ),
    ]
