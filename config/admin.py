# -*- coding: UTF-8 -*-
"""
@Author  ：dongli
@File    ：admin.py
@Time    ：2021/7/4 10:23
"""
from django.contrib import admin
from .models import Link, SideBar


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    """
    :author:  dongli
    :title:  LinkAdmin-友链配置后台
    :remark:
    :time:  2021/7/6 20:18
    """
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')

    def save_model(self, request, obj, form, change):
        """
        :author:  dongli
        :title:  友链创建者默认当前登录用户
        :remark:  request.user--当前登录用户
        :time:  2021/7/4 09:37
        """
        obj.owner = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)


@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    """
    :author:  dongli
    :title:  SideBarAdmin-侧边栏配置后台
    :remark:
    :time:  2021/7/6 20:20
    """
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')

    def save_model(self, request, obj, form, change):
        """
        :author:  dongli
        :title:  友链创建者默认当前登录用户
        :remark:  request.user--当前登录用户
        :time:  2021/7/4 09:37
        """
        obj.owner = request.user
        return super(SideBarAdmin, self).save_model(request, obj, form, change)
