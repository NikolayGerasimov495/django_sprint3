from django.db import models
from django.contrib.auth import get_user_model
from core.models import PublishedModel

TITLE_MAX_LENGTH = 256

User = get_user_model()


class Category(PublishedModel):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=TITLE_MAX_LENGTH)
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        verbose_name='Идентификатор',
        unique=True,
        help_text=("Идентификатор страницы для URL; разрешены символы "
                   "латиницы, цифры, дефис и подчёркивание."))

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:10]


class Location(PublishedModel):
    name = models.CharField(
        verbose_name='Название места',
        max_length=TITLE_MAX_LENGTH)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name[:10]


class Post(PublishedModel):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=TITLE_MAX_LENGTH)
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=("Если установить дату и время в будущем — можно делать "
                   "отложенные публикации."))
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title[:10]
