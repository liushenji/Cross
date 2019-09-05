# encoding: utf-8
"""
@author: victory Liu
@contact: mrliushenji@163.com
@time: 2019/8/29 14:55
@file: basemodel.py
@desc: 
"""
from django.db import models


class BaseModel(models.Model):
    create_at = models.DateTimeField(null=True, blank=True)
    update_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        # 说明这是一个抽象模型类
        abstract = True
