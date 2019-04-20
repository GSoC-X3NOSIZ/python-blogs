# Generated by Django 2.1.8 on 2019-04-20 01:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import gsoc.models


class Migration(migrations.Migration):

    dependencies = [
        ('gsoc', '0013_pagenotification'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddUserLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_id', models.CharField(default=gsoc.models.gen_uuid_str, max_length=36)),
            ],
            options={
                'verbose_name': 'Add Users(The invites will be sent to the emails on save)',
                'verbose_name_plural': 'Add Users(The invites will be sent to the emails on save)',
            },
        ),
        migrations.AlterModelOptions(
            name='gsocyear',
            options={'ordering': ['-gsoc_year']},
        ),
        migrations.AddField(
            model_name='reglink',
            name='email',
            field=models.CharField(default='', max_length=300, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AddField(
            model_name='reglink',
            name='scheduler',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='gsoc.Scheduler'),
        ),
        migrations.AddField(
            model_name='reglink',
            name='adduserlog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reglinks', to='gsoc.AddUserLog'),
        ),
    ]