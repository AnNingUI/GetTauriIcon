#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: temp: 潘高, AnNingUI
LastEditors: AnNingUI
Date: 2023-03-12 20:08:30
LastEditTime: 2024-01-22 17:08:27
Description: 操作数据库类
usage:
    from api.db.orm import ORM

    orm = ORM()    # 操作数据库类
    author = self.orm.getStorageVar('author')    # 获取储存变量
    print('author', author)
'''

from api.db.models import PPXStorageVar
from pyapp.db.db import DB
from sqlalchemy import Column, select, update, insert
from typing import Optional

class ORM:
    '''操作数据库类'''

    def getStorageVar(self, key: Column[str]):
        '''获取储存变量'''
        resVal: str = ''
        dbSession = DB.session()
        with dbSession.begin():
            stmt = select(PPXStorageVar.val).where(PPXStorageVar.key == key)
            result = dbSession.execute(stmt)
            # Result[Tuple[str]]
            result = result.one_or_none()
            # result: (Row[Tuple[str]] | None)
            if result is None:
                # 新建
                stmt = insert(PPXStorageVar).values(key=key)
                # stmt: Insert
                dbSession.execute(stmt)
            else:
                resVal = result[0]
                # resVal: ?
        dbSession.close()
        return resVal

    def setStorageVar(self, key: Column[str], val: str):
        '''更新储存变量'''
        dbSession = DB.session()
        with dbSession.begin():
            stmt = update(PPXStorageVar).where(PPXStorageVar.key == key).values(val=val)
            dbSession.execute(stmt)
        dbSession.close()
