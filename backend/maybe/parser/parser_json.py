#-*-coding:utf-8-*-

'''
# ----------------------------------------------------------------------------
#    Purpose:     用于获取数据源文件
#
#    Author:      半片叶
#
#    Created:     2020.06.10
#
#    ██╗   ██╗  ███████╗
#    ╚██╗ ██╔╝  ██╔════╝
#     ╚████╔╝   █████╗
#      ╚██╔╝    ██╔══╝
#       ██║     ███████╗
#       ╚═╝     ╚══════╝
# ----------------------------------------------------------------------------
'''

import json
import logging


logger = logging.getLogger(__name__)


class parserJsonFile():
    def __init__(self, source_file:str):
        """
        json文件解析器
            外部参数:
                :param source_file: json文件路径
            内部参数:
                :private json_data: 解析所得json数据内容
                :private message:解析结果消息
        """
        self.source_file = source_file
        self.json_data = {}
        self.message = ""

    def read(self) -> bool:
        """
        读取json文件内容
            :return: 解析是否成功的结果
        """
        with open(self.source_file, 'r', encoding="utf-8") as fread:
            try:
                self.json_data = json.load(fread)
            except json.JSONDecodeError as error:
                logger.error(f"{self.source_file}文件解析失败:{error}")
                self.message = error
                return False
        return True

    def parser(self):
        """
        解析json数据内容，可支持Dict对象内容或者List对象内容
        """
        if self.read():
            if isinstance(self.json_data, dict):
                self.parser_dict(self.json_data)
            elif isinstance(self.json_data, list):
                self.parser_list(self.json_data)
            else:
                self.message = "只支持解析Dict或者List对象！"

    def parser_dict(self, content):
        """
        解析字典对象内容
            :param content: json文件内容
        :return:
        """
        pass

    def parser_list(self, content):
        """
        解析列表对象内容
            :param content: json文件内容
        :return:
        """
        pass



if __name__ == '__main__':
    p = parserJsonFile("../../datas/myProjectSet.json")
    p.parser()
