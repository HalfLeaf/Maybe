#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     创建数据库数据
#
#  Author:      半片叶
#
#  Created:     2020.08.28
#
#        _       __    _     ___   ____
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

from datetime import datetime
from models.mongo_client import MongoDatabase

class CreatedDatabaseData():
    def __init__(self):
        self.db = MongoDatabase().db

    def create(self):
        self.db.bool_instance.insert_one({
            "field":"invalid",
            "value":"undefined",
            "status":1,
            "creator":"yewei8",
            "create_time":datetime.utcnow()
        })



if __name__ == '__main__':
    c = CreatedDatabaseData()
    c.create()
