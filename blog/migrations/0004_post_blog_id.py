# Generated by Django 3.2.18 on 2024-01-18 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_encodings'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_id',
            field=models.CharField(default=' fjwoie', max_length=100),
            preserve_default=False,
        ),
    ]
