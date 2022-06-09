from django.db import models


class Word(models.Model):
    spell = models.CharField(max_length=40, verbose_name='拼写', unique=True)
    pron = models.CharField(max_length=40, verbose_name='音标', null=True, blank=True)
    zh = models.CharField(max_length=40, verbose_name='汉译', null=True, blank=True)
    en = models.CharField(max_length=40, verbose_name='英译', null=True, blank=True)
    remark = models.CharField(max_length=400, verbose_name='备注', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='创建日期')

    def __str__(self):
        return self.spell
