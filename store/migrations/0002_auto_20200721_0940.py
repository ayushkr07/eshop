# Generated by Django 3.0.8 on 2020-07-21 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cateogory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='upload/product/'),
        ),
        migrations.AddField(
            model_name='product',
            name='cateogory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.Cateogory'),
        ),
    ]
