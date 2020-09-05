# -*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#  Purpose:     项目日志配置
#
#  Author:      半片叶
#
#  Created:     2020.08.12
#
#        _       __    _     ___   ____
#       | |\/|  / /\  \ \_/ | |_) | |_
#       |_|  | /_/--\  |_|  |_|_) |_|__
# ----------------------------------------------------------------------------
'''

import logging
from pathlib import Path
from datetime import datetime
now = datetime.now().strftime("%Y%m%d-%H%M")
path = Path(f'logs')
path.mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] - << %(filename)s %(funcName)s line:%(lineno)d >> [%(levelname)s] - %(message)s',
                    datefmt='%d-%b-%Y %H:%M:%S',
                    filename=f'logs/maybe-{now}.log',
                    filemode='w')