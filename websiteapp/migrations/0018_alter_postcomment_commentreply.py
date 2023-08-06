# Generated by Django 4.2 on 2023-06-29 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0017_postcomment_commentreply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='commentreply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='websiteapp.postcomment'),
        ),
    ]
