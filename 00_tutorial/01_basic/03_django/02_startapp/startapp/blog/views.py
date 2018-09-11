from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from django.utils import timezone
from .forms import PostForm

def post_list(request):
    qs = Post.objects.all()
    qs.filter(published_date__lte=timezone.now())
    qs.order_by('published_date')
    return render(request, 'blog/post_list.html', {
        'post_list':qs
    })

# from django.http import JsonResponse

    # data = {
    #     'post': {
    #         'title':post.title,
    #         'text':post.text,
    #         'published_date':post.published_date
    #     }
    # }
    # return JsonResponse(data)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post':post
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)

    else:
        form = PostForm()
    return render(request, 'blog/post_forms_edit.html', {
        'form':form
    })