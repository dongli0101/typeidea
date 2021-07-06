# -*- coding: UTF-8 -*-
"""
@Author  ：dongli
@File    ：admin.py.py
@Time    ：2021/7/3 19:46 
"""
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    :author:  dongli
    :title:  CategoryAdmin-分类后台
    :remark:  TODO:obj是什么？
    :time:  2021/7/3 19:47
    """
    list_display = ('name', 'post_count', 'status', 'is_nav', 'owner', 'created_time')
    # fields = ('name', 'status', 'is_nav', 'owner')
    fields = ('name', 'status', 'is_nav')

    def save_model(self, request, obj, form, change):
        """
        :author:  dongli
        :title:  分类创建者默认当前登录用户
        :remark:  TODO:super().save_model方法的作用？
            1.request.user--当前登录用户
        :time:  2021/7/3 20:36
        """
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def post_count(self, obj):
        """
        :author:  dongli
        :title:  统计分类下的文章数量
        :remark:  TODO：post_set是怎么来的？
        :time:  2021/7/4 10:13
        """
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    :author:  dongli
    :title:  TagAdmin-标签后台
    :remark:
    :time:  2021/7/3 19:52
    """
    list_display = ('name', 'post_count', 'status', 'owner', 'created_time')
    # fields = ('name', 'status', 'owner')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        """
        :author:  dongli
        :title:  标签创建者默认当前登录用户
        :remark:  request.user--当前登录用户
        :time:  2021/7/3 20:30
        """
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)

    def post_count(self, obj):
        """
        :author:  dongli
        :title:  统计标签下的文章数量
        :remark:
        :time:  2021/7/4 10:16
        """
        return obj.post_set.count()

    post_count.short_description = '文章数量'


class CategoryOwnerFilter(admin.SimpleListFilter):
    """
    :author:  dongli
    :title:  自定义过滤器只展示当前用户分类
    :remark:  TODO：Category.objects是什么？为什么直接就能过滤
    :time:  2021/7/4 17:59
    """
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    :author:  dongli
    :title:  PostAdmin-文章后台
    :remark:
    :time:  2021/7/6 20:32
    """
    # 配置列表展示
    list_display = ['title', 'category', 'status', 'owner', 'created_time', 'operator']
    # list_display = ['title', 'category', 'status', 'created_time', 'operator']
    # 配置编辑字段链接
    list_display_links = []
    # 配置页面列表过滤器，以下根据分类和标签分组过滤
    list_filter = [CategoryOwnerFilter, 'tag']
    # 配置搜索字段
    search_fields = ['title', 'category__name']
    # 动作相关配置，是否展示在顶部
    actions_on_top = True
    # 动作相关配置，是否展示在底部
    # actions_on_bottom = True

    # 编辑页面：保存/编辑/编辑并新建是否在顶部展示
    # save_on_top = True
    # 新建/编辑/编辑并新建页面展示字段，元祖内表示显示在同一行，其他的按列显示
    fields = (
        ('category', 'title'),
        # 'category',
        # 'title',
        'desc',
        'status',
        'content',
        'tag',
    )

    def operator(self, obj):
        """
        :author:  dongli
        :title:  操作项-编辑
        :remark:
            1.TODO:format_html的reverse是啥？
            2.TODO:get_queryset调用原理？
        :time:  2021/7/4 09:36
        """
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        """
        :author:  dongli
        :title:  文章创建者默认当前登录用户
        :remark:  request.user--当前登录用户
        :time:  2021/7/4 09:37
        """
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
        :author:  dongli
        :title:  过滤文章所属者查看
        :remark:  request.user--当前登录用户
        :time:  2021/7/6 19:37
        """
        owner_filter = super(PostAdmin, self).get_queryset(request)
        return owner_filter.filter(owner=request.user)
