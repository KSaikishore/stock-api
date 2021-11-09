# Generated by Django 3.2.8 on 2021-11-08 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='createdAt')),
                ('createdBy', models.IntegerField(default=0)),
                ('modifiedAt', models.DateTimeField(auto_now=True, verbose_name='modifiedAt')),
                ('modifiedBy', models.IntegerField(default=0)),
                ('stock_symbol', models.CharField(max_length=20)),
                ('security_name', models.CharField(max_length=300)),
                ('quantity', models.IntegerField(default=100)),
                ('price', models.IntegerField(default=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='createdAt')),
                ('createdBy', models.IntegerField(default=0)),
                ('modifiedAt', models.DateTimeField(auto_now=True, verbose_name='modifiedAt')),
                ('modifiedBy', models.IntegerField(default=0)),
                ('Type', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell'), ('ongoing', 'Ongoing')], max_length=200)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.stock')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='createdAt')),
                ('createdBy', models.IntegerField(default=0)),
                ('modifiedAt', models.DateTimeField(auto_now=True, verbose_name='modifiedAt')),
                ('modifiedBy', models.IntegerField(default=0)),
                ('transactions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.transaction')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
