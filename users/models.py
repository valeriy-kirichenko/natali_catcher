from typing import List, Tuple
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель для пользователей.

        В качестве логина будет использоваться email, поля ('username',
        'first_name') обязательны к заполнению.
        send_messages отвечает за рассылку пользователям сообщений о
        поступлении новых изделий.

    Attributes:
        username (str): имя пользователя.
        password (str): пароль.
        email (str): электронная почта.
        first_name (str): имя.
        last_name (str): фамилия.
        send_messages (bool): флаг для рассылки сообщений.
    """

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: List[str] = ['username', 'first_name']
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        help_text='Введите имя пользователя'
    )
    password = models.CharField(
        'Пароль', max_length=254, help_text='Введите пароль'
    )
    email = models.EmailField(
        'Электронная почта',
        unique=True,
        max_length=254,
        help_text='Введите электронную почту'
    )
    first_name = models.CharField(
        'Имя', max_length=150, help_text='Введите имя'
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        help_text='Введите фамилию',
        blank=True
    )
    send_messages = models.BooleanField(
        'Рассылка',
        default=False,
    )

    class Meta:
        ordering: Tuple[str] = ('id',)
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователи'

    def __str__(self):
        """Возвращает строковое представление модели"""

        return self.username
