from django.utils import timezone
from blog.models import Post


def get_published_posts():
    return Post.objects.select_related('category', 'author').filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True)
