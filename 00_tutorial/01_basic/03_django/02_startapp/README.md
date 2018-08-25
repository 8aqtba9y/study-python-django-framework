# 02_startapp

02_startapp

先行: 01_startproject

## command

### プロジェクト内にappを生成

`$ python manager.py startapp blog`

### プロジェクト内にappを追加／定義

startapp/settings.py
```
INSTALLED_APPS = [ # 33行目
    ...
    'blog',
]
```