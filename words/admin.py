from django.contrib import admin

from .models import Word
from .models import Sentence


class SentenceInline(admin.StackedInline):
    model = Sentence
    fields = ('context',)


class WordAdmin(admin.ModelAdmin):
    list_display = ('spell', 'pron', 'zh', 'en', 'remark', 'create_date')
    inlines = [SentenceInline]


class SentenceAdmin(admin.ModelAdmin):
    list_display = ('word', 'context', 'translation', 'create_date')


admin.site.register(Word, WordAdmin)
admin.site.register(Sentence, SentenceAdmin)
