# -*- coding: UTF-8 -*-
"""
@Author  ：dongli
@File    ：admin.py
@Time    ：2021/7/4 10:23 
"""
from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')