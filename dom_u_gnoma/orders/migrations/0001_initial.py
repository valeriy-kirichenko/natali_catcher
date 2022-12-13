# Generated by Django 4.1.3 on 2022-12-09 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0006_delete_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(help_text='Введите вашу фамилию', max_length=150, verbose_name='Фамилия')),
                ('first_name', models.CharField(help_text='Введите ваше имя', max_length=150, verbose_name='Имя')),
                ('middle_name', models.CharField(help_text='Введите ваше отчество', max_length=150, verbose_name='Отчество')),
                ('city', models.CharField(help_text='Введите название вашего города', max_length=150, verbose_name='Город')),
                ('street', models.CharField(help_text='Введите название вашей улицы', max_length=150, verbose_name='Улица')),
                ('house', models.CharField(help_text='Номер Дома/Корпуса/Строения', max_length=150, verbose_name='Дом/Корпус/Строение')),
                ('postal_code', models.CharField(help_text='Введите ваш почтовый индекс', max_length=6, verbose_name='Почтовый индекс')),
                ('phone', models.CharField(help_text='Введите ваш телефон', max_length=11, verbose_name='Телефон')),
                ('email', models.EmailField(help_text='Введите вашу электронную почту', max_length=254, verbose_name='Электронная почта')),
                ('payed', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item', verbose_name='Изделие')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Изделия в заказе',
                'verbose_name_plural': 'Изделия в заказе',
                'ordering': ('-order',),
            },
        ),
    ]