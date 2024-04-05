# CodePET

## About
Тестовое задание для CodePET

## Stack:
* Django
* DRF
* PostgreSQL
* Docker + Docker-compose
* Gunicorn
---
# Develop:

Для разработки требуется [vscode](https://code.visualstudio.com/) и [vscode-remote-containers](https://code.visualstudio.com/docs/remote/containers).

### Config
Для генерации конфига:
```bash
./deploy.sh config
```
Создастся файл `.env`, в котором нужно указать все необходимые данные. Так же создастся файл `kernel/config/local_settings.py`, в котором нужно указать домен и данные CORS.


### Codding

Для разработки бэкенда с помощью django откройте проект django в vscode и снова откройте его в контейнере.


```bash
code kernel
```

![reopen](https://github.com/lyaguxafrog/python-backend-devcontainers/blob/release/docs/pics/reopen.png?raw=true)

Для миграции:
```bash
./manage.sh migrate
```

Чтобы создать новое djangо-приложение:
```bash
./manage.sh app
```
---

## Codestyle
```python
# -*- coding: utf-8 -*-

# Сначала импорт общих модулей
import os
import sys
import json

# Django модули
from django.db import models

# Затем django-библиотеки
from graphene_django import DjangoObjectType

# И в конце локальные модули
from app.models import MyModel


class SomeClass:
    """ Описание класса """

    def t_sum(self, first_num: int, second_num: int) -> int:
        """
        Метод сложения двух чисел.

        :param first_num: Первое число
        :param second_num: Второе число

        :returns: Возвращает сумму двух чисел.
        """

        return sum(first_num, second_num)


class AnotherClass:
    """
    Длинное описание класса
    """
    pass
```
Отступы: четыре пробела. Максимальная длинна строки: 80 символов.




---
# Deploy

Для деплоя нужно

1. Создать конфиг
```
./deploy.sh config
```
Создастся файл `.env`, в котором нужно указать все необходимые данные. Так же создастся файл `kernel/config/local_settings.py`, в котором нужно указать домен и данные CORS.

2. Запустить
```
./deploy.sh 
```




&copy; Gen by [PBD](https://gitub.com/lyaguxafrog/python-backend-devcontainers) with 💚
