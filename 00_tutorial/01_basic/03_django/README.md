# 03_django
03_django

### コマンド一覧

`$ django-admin startproject <projectname> .`

`$ python manage.py migrate`

`$ python manager.py startapp <appname>`

`$ python manage.py makemigrations <appname>`

`$ python manage.py migrate <appname>`

### VSコードの初期設定

`$ pip install pylint-django`

`「Command」＋「,」`

USER SETTINGS
```
{
    …,
    "python.linting.pylintArgs": [
        "--load-plugins",
        "pylint_django"
    ]
}
```