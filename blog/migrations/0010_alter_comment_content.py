# Generated by Django 4.2.4 on 2023-08-29 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_category_id_alter_post_id_alter_tag_id_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
    ]