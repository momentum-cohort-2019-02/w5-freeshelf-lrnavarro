# Generated by Django 2.1.7 on 2019-03-18 01:58

from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0006_auto_20190317_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
            preserve_default=False,
        ),
    ]
