# FORMS.md

FORMS.md

先行:

 [02_startapp/README.md](./README.md)

 [02_startapp/CSS.md](./CSS.md)

 [02_startapp/APP.md](./APP.md)

## 1. FORMS

### formsを定義

##### formsを追加

blog/forms.py
```
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
```


##### urlを追加

blog/urls.py
```
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
```


blog/views.py
```
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.utils import timezone
from .forms import PostForm

...

def post_new(request):
    pass
```

![](startapp/screenshots/14_add_forms.png)

