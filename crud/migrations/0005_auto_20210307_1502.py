# Generated by Django 3.1.7 on 2021-03-07 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('crud', '0004_crudcomment_infocomment_qnacomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crud',
            name='name',
        ),
        migrations.AddField(
            model_name='crud',
            name='profile_id',
            field=models.ForeignKey(db_column='profile_id', default=15, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='account.profile'),
            preserve_default=False,
        ),
    ]
