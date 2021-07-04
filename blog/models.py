# -*- coding: UTF-8 -*-
"""
@Author  ：dongli
@File    ：models.py
@Time    ：2021/6/27 21:19
"""
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    """
    :author:  dongli
    :title:  blog-分类
    :remark:  TODO
    :time:  2021/6/27 22:22
    """

    def __str__(self):
        """
        :author:  dongli
        :title:  增加配置类，调用方显示Category对象实例名称
        :remark:  TODO
        :time:  2021/7/4 09:59
        """
        return self.name

    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(
        default=STATUS_NORMAL,
        choices=STATUS_ITEMS,
        verbose_name=' 状态'
    )
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    """
    :author:  dongli
    :title:  blog-标签
    :remark:  TODO
    :time:  2021/6/27 22:22
    """

    def __str__(self):
        """
        :author:  dongli
        :title:  增加配置类，调用方显示Tag对象实例名称
        :remark:  TODO
        :time:  2021/7/4 09:59
        """
        return self.name

    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=10, verbose_name='名称')
    status = models.PositiveIntegerField(
        default=STATUS_NORMAL,
        choices=STATUS_ITEMS,
        verbose_name=' 状态'
    )
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):
    """
    :author:  dongli
    :title:  blog-文章
    :remark:  TODO
    :time:  2021/6/27 22:24
    """

    def __str__(self):
        """
        :author:  dongli
        :title:  增加配置类，调用方显示Category对象实例名称
        :remark:  TODO
        :time:  2021/7/4 09:59
        """
        return self.title

    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )

    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正文必须为MarkDown格式')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS,
                                         verbose_name='状态'
                                         )

    owner = models.ForeignKey(User, verbose_name='作者')
    tag = models.ForeignKey(Tag, verbose_name='标签')
    category = models.ForeignKey(Category, verbose_name='分类')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']  # 根据id进行降序
