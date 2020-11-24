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

+ Створив новий Django додаток head
```
pipenv run python manage.py startapp head

```
+ Створив нову директорію `./head/templates`, створено файли `./head/templates/index.html` та `./head/urls.py`

