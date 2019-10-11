# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 15:45
# @Author  : DannyDong
# @File    : webhook.py
# @describe: 接通钉钉机器人通知

import json
import requests

from Utils.read_ini import ReadIni


class WebHook(object):
    def __init__(self):
        self.url = ReadIni('Sys_config.ini', 'WEBHOOK').get_value('web_hook_url')

    def web_hook(self, text, mobile):
        url = self.url
        program = {
            "msgtype": "text",
            "text": {"content": text},
            "at": {
                "atMobiles": mobile,
                "isAtAll": False
            }
        }
        headers = {'Content-Type': 'application/json'}
        requests.post(url, data=json.dumps(program), headers=headers)
