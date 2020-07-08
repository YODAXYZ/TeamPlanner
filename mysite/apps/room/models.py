from django.db import models
import datetime
from django.utils import timezone


class Room(models.Model):
    room_title = models.CharField('Name of title', max_length=200)
    room_text = models.TextField('Some info')
    pub_date = models.DateTimeField("Date of publication")

    def __str__(self):
        return self.room_title

    def recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'




# class Comment(models.Model):
#     article = models.ForeignKey(Room, on_delete=models.CASCADE) # cascade удаленные комментарии к статье
#     author = models.CharField("Name of author", max_length=30)
#     comment_text = models.CharField('Text of comment', max_length=200)


