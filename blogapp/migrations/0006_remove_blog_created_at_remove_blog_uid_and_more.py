# Generated by Django 4.1 on 2023-01-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_rename_blog_text_blog_blog_text_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='blog',
            name='id',
            field=models.BigAutoField(auto_created=True, default=11, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
