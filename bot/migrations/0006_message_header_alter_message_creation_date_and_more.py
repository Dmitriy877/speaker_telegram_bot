# Generated by Django 5.2 on 2025-05-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='header',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Текст заголовка'),
        ),
        migrations.AlterField(
            model_name='message',
            name='creation_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Текст сообщения'),
        ),
        migrations.AlterField(
            model_name='message',
            name='recipent',
            field=models.ManyToManyField(default=None, related_name='messages', to='bot.participant', verbose_name='Кому отправлено'),
        ),
        migrations.AlterField(
            model_name='message',
            name='send_status',
            field=models.BooleanField(default=False, verbose_name='Отправлено'),
        ),
    ]
