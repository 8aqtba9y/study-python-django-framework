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

### django appのモデルを定義

startapp/blog/models.py
```
from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model) :
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self) :
        self.published_date = timezone.now()
        self.save
    
    def __str__(self) :
        return self.title

```

### 定義したモデルをデータベースに保存

`$ python manage.py makemigrations blog`

`$ python manage.py migrate blog`

### 言語コードを編集

startapp/settings.py
```
LANGUAGE_CODE = 'ko-kr' # 107行目
```

![](startapp/screenshots/01_admin.png)

### スーパーユーザーを生成

`python manage.py createsuperuser`

![](startapp/screenshots/02_admin_login.png)

### Postモデルをadminに登録

startapp/blog/admin.py
```
from django.contrib import admin
from .models import Post


# Register your models here.

admin.site.register(Post)
```

![](startapp/screenshots/03_register_post_model.png)