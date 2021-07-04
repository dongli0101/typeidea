# -*- coding: UTF-8 -*-
"""
@Author  ：dongli
@File    ：models.py
@Time    ：2021/7/03 09:54
"""
from django.db import models
from blog.models import Post


class Comment(models.Model):
    """
    :author:  dongli
    :title:  comment-评论
    :remark:  TODO
    :time:  2021/7/3 09:55
    """
    def __str__(self):
        """
        :author:  dongli
        :title:  增加配置类，调用方显示Comment对象实例名称
        :remark:  TODO
        :time:  2021/7/4 10:38
        """
        return self.content

    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    target = models.ForeignKey(Post, verbose_name='评论目标（文章）')
    content = models.CharField(max_length=2000, verbose_name='内容')
    nickname = models.CharField(max_length=50, verbose_name='昵称（用户名）')
    website = models.URLField(verbose_name='网站')
    email = models.EmailField(verbose_name='邮箱')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '评论'
