# Lab_3: Вступ до моніторингу.

+ Створив віртуальне середовище, встановив Django
```
pipenv --python 3.6
pipenv install django
```
+ Створив template проекту з назвою adventure,виніс створені файли на рівень вище.
```
pipenv run django-admin startproject adventure

mv adventure/adventure/* adventure/
mv adventure/manage.py ./
``` 
+  Запустив Django сервер
```
pipenv run python manage.py runserver
```
Локальний сервер запущено на порті: 8000


