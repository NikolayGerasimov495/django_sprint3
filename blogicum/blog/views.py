from django.shortcuts import get_object_or_404, render
from .models import Post, Category
from django.utils import timezone


def index(request):
    """Представление главной страницы блога"""
    post_list = Post.objects.select_related('category', 'location',
                                            'author').\
        filter(pub_date__lte=timezone.now(),
               is_published=True,
               category__is_published=True)[:5]
    context = {'post_list': post_list,
               }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Педставление страницы поста"""
    post = get_object_or_404(Post.objects.filter(pub_date__lte=timezone.now(),
                                                 is_published=True,
                                                 category__is_published=True),
                             pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Представление категорий поста"""
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True)

    posts = Post.objects.select_related('category', 'author').\
        filter(category__slug=category_slug,
               pub_date__lte=timezone.now(), is_published=True)

    context = {'post_list': posts,
               'category': category}
    return render(request, 'blog/category.html', context)
