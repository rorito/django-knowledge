# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from knowledge.models import Question, Response, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]
    prepopulated_fields = {'slug': ('title', )}
admin.site.register(Category, CategoryAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Question._meta.fields]
    list_select_related = True
    raw_id_fields = ['user']
admin.site.register(Question, QuestionAdmin)


class ResponseAdmin(admin.ModelAdmin):
    def admin_body(self, obj):
        return obj.body[:150]

    admin_body.short_description = _(u'Ответ')
    admin_body.allow_tags = True

    list_display = ['pk', 'admin_body', 'question', 'added', 'status', 'accepted']
    list_display_links = ['pk', 'admin_body']
    list_filter = ['question', 'status', 'accepted']
    list_select_related = True
    raw_id_fields = ['user', 'question']
admin.site.register(Response, ResponseAdmin)
