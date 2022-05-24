# Generated by Django 3.2.8 on 2022-02-19 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZeBarTools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='zebartools_image/%Y/%m/', verbose_name='Main foto')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'ZeBarTools',
                'verbose_name_plural': 'ZeBarTools',
            },
        ),
        migrations.AlterField(
            model_name='icetype',
            name='image',
            field=models.ImageField(default='', upload_to='ice_type_image/%Y/%m/', verbose_name='Main foto'),
        ),
        migrations.CreateModel(
            name='ZeBarToolsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='photos/zebartools_photo/%Y/%m/', verbose_name='Image')),
                ('zebartools_item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.zebartools')),
            ],
        ),
    ]
