# Generated by Django 4.2 on 2023-06-29 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0016_moviedetailpage_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='commentreply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='websiteapp.postcomment'),
        ),
    ]