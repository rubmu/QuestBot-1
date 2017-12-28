# Generated by Django 2.0 on 2017-12-28 19:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_auto_20171225_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='move_user_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Step', verbose_name='Mover user to step'),
        ),
        migrations.AlterField(
            model_name='event',
            name='send_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time to send on'),
        ),
    ]