#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: temp: 潘高, AnNingUI
LastEditors: AnNingUI
Date: 2022-03-21 17:01:39
LastEditTime: 2024-09-08 20:28:48
Description: 业务层API，供前端JS调用
usage: 在Javascript中调用window.pywebview.api.<methodname>(<parameters>)
'''

from api.storage import Storage
from api.system import System
from api.tauri_icon import TauriIcon
from webview import Window

class API(
    System, 
    Storage,
    TauriIcon
):
    '''业务层API，供前端JS调用'''

    def setWindow(self, window: Window):
        '''获取窗口实例'''
        System._window = window
