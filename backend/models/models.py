#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     数据库存储模型定义
#
#  Author:      半片叶
#
#  Created:     2020.08.19
#        _       __    _     ___   ____
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

from mongoengine import (Document, BooleanField, StringField, UUIDField, FloatField,
                         ReferenceField, IntField, ListField, DateTimeField, DictField)


class DataInstance(Document):
    # 数据实例名称
    name = StringField()
    # 分类，来源
    # python - Python基本数据类型
    # common - 常用属性对象
    # custom - 用户自定义对象
    source = StringField()
    # 默认值
    default_value = ListField()
    # 用户经验值
    experience_value = ListField()

class ExperienceData(Document):
    # 数据实例名称
    name = StringField()
    # 用户经验值
    experience_value = ListField()

