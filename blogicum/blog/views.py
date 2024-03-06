from django.shortcuts import get_object_or_404, render
from blog.models import Category
from core.get_published_posts import get_published_posts


def index(request):
    """Представление главной страницы блога"""
    post_list = get_published_posts()[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Педставление страницы поста"""
    post = get_object_or_404(get_published_posts(), pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Представление категорий поста"""
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True)
    posts = get_published_posts().filter(category__slug=category_slug)
    context = {'post_list': posts, 'category': category}
    return render(request, 'blog/category.html', context)
