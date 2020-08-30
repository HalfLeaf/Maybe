#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     BOOL类型实例对象
#
#  Author:      半片叶
#
#  Created:     2020.08.11
#
#        _       __    _     ___   ____
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

from typing import Any
from models.mongo_client import MongoDatabase

class BoolData():
    def __init__(self):
        """
        Bool类型测试数据
            外部参数:
                无
            内部参数:
                :private _effective:有效域值缓存对象
                :private _invalid:无效域值缓存对象
                :private _experience:推测域值缓存对象
        """
        self.db = MongoDatabase().db
        self._effective = None
        self._invalid = None
        self._experience = None

    def get(self, field="") -> Any:
        """
        获取bool类型值
            外部参数:
                :param field:指定的参数域
            返回值:
        """
        if field == "invalid":
            return self._get_invalid_field()
        elif field == "experience":
            return self._get_experience_field()
        else:
            return self._get_effective_field()

    def _get_effective_field(self) -> bool:
        """
        获取Bool类型的有效域
            外部参数:
                无
            返回值:
                正确的Python Bool类型数据
        """
        if not self._effective:
            self._effective = [x.get('value') for x in list(self.db.bool_instance.find({"field":"effective", "status":1}, {"value":1}))]
        return self._effective

    def _get_invalid_field(self) -> bool:
        """
        获取Bool类型的无效域
            外部参数:
                无
            返回值:
                正确的Python Bool类型数据
        """
        if not self._invalid:
            self._invalid = [x.get('value') for x in list(self.db.bool_instance.find({"field":"invalid", "status":1}, {"value":1}))]
        return self._invalid

    def _get_experience_field(self) -> bool:
        """
        获取Bool类型的推测域
            外部参数:
                无
            返回值:
                正确的Python Bool类型数据
        """
        if self._experience:
            self._experience = [x.get('value') for x in list(self.db.bool_instance.find({"field":"experience", "status":1}, {"value":1}))]
        return self._experience