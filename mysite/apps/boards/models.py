from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="board", null=True)
    board_title = models.CharField('Name of title', max_length=200)
    # board_text = models.TextField('Some info')
    # teammates = ...  # юзеры, у которых есть доступ
    pub_date = models.DateTimeField("Date of publication")

    def __str__(self):
        return self.board_title

    def recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'
