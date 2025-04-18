#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: temp: 潘高, AnNingUI
LastEditors: AnNingUI
Date: 2023-03-25 19:39:03
LastEditTime: 2024-12-17 14:06:00
Description: 操作存储在数据库中的数据
usage: 调用window.pywebview.api.storage.<methodname>(<parameters>)从Javascript执行
'''

from api.db.orm import ORM


class Storage():
    '''存储类'''

    orm = ORM()    # 操作数据库类

    def storage_get(self, key: str) -> str:
        '''获取关键词的值'''
        return self.orm.getStorageVar(key)

    def storage_set(self, key: str, val: str):
        '''设置关键词的值'''
        self.orm.setStorageVar(key, val)
