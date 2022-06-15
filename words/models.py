from django.db import models


class Word(models.Model):
    spell = models.CharField(max_length=40, verbose_name='拼写', unique=True)
    prefix = models.CharField(max_length=40, verbose_name='前缀', null=True, blank=True)
    suffix = models.CharField(max_length=40, verbose_name='后缀', null=True, blank=True)
    pron = models.CharField(max_length=40, verbose_name='音标', null=True, blank=True)
    zh = models.CharField(max_length=400, verbose_name='汉译', null=True, blank=True)
    en = models.CharField(max_length=400, verbose_name='英译', null=True, blank=True)
    remark = models.CharField(max_length=400, verbose_name='备注', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

    def __str__(self):
        return self.spell


class Sentence(models.Model):
    """和单词是多对一的关系"""
    word = models.ForeignKey('Word', on_delete=models.CASCADE)
    context = models.CharField(max_length=400, verbose_name='句子', null=True, blank=True)
    translation = models.CharField(max_length=400, verbose_name='译文', null=True, blank=True)
    remark = models.CharField(max_length=400, verbose_name='备注', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

    def __str__(self):
        return f'{self.context[:20]}......' if len(self.context) >= 30 else self.context
