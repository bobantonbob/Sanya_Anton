from django.db import models
from django.utils import timezone
import pytz

class Application(models.Model):

    name = models.CharField("Ім'я", max_length=15)
    email = models.EmailField('Email', max_length=30, unique=False)
    phone = models.CharField('Телефон', max_length=20, unique=True)
    subject = models.TextField('Тема', max_length=256, null=False)
    message = models.TextField('Повідомлення', max_length=1024, null=True)
    timestamp = models.DateTimeField('Час', auto_now_add=True, null=False)



    def __str__(self):
        return self.phone


