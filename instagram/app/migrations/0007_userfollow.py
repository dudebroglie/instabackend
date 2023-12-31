# Generated by Django 4.2.3 on 2023-07-16 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_postcomment_post_alter_postlike_post_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follows', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dest_follow', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='src_follow', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
