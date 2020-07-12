from django.conf import settings
from django.db import models


class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Comment(models.Model):
    article = models.ForeignKey(Task, on_delete=models.CASCADE)  # cascade удаленные комментарии к таску
    author = models.CharField("Name of author", max_length=30)
    comment_text = models.CharField('Text of comment', max_length=200)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
