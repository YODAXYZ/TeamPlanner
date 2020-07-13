from django.db import models


class Column(models.Model):
    column_title = models.CharField('Name of title', max_length=200)
    task_list = []  # изменить на что-то каноничное

    def __str__(self):
        return self.column_title

    class Meta:
        verbose_name = 'Колонка'
        verbose_name_plural = 'Колонки'