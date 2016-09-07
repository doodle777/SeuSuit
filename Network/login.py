# -*= coding:utf-8 -*-

from http import cookiejar
from urllib import request as Req
from urllib import parse
import base64
import json


class Login:
    def __init__(self):
        self.username   = '220151538'
        self.password   = 'dx2010001'
        self.login_url  = 'https://w.seu.edu.cn/index.php/index/login'
        self.logout_url = 'https://w.seu.edu.cn/index.php/index/logout'
        self.cookies    = cookiejar.CookieJar()
        self.opener     = Req.build_opener(Req.HTTPCookieProcessor(self.cookies))

    def login(self):
        data = parse.urlencode({
            'username': self.username,
            'password': base64.b64encode(self.password.encode('utf-8')),
            'enablemacauth': '0'
        }).encode('ascii')

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Ecoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Connection': 'keep-alive',
            # 'Content-Length':   '126',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie':           'ASP.NET_SessionId=bi0p2y45h05p4evtewbx4245',
            'DNT': '1',
            'Host': 'w.seu.edu.cn',
            'Origin': 'https://w.seu.edu.cn',
            'Referer': 'https://w.seu.edu.cn/',
            'User-Agent': 'Chrome/52.0.2743.116 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        request = Req.Request(url=self.login_url, data=data, headers=headers)
        response = self.opener.open(request)
        result = response.read().decode('unicode_escape')
        print(result)

    def logout(self):

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Ecoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Connection': 'keep-alive',
            # 'Content-Length':   '126',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie':           'ASP.NET_SessionId=bi0p2y45h05p4evtewbx4245',
            'DNT': '1',
            'Host': 'w.seu.edu.cn',
            'Origin': 'https://w.seu.edu.cn',
            'Referer': 'https://w.seu.edu.cn/',
            'User-Agent': 'Chrome/52.0.2743.116 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        request = Req.Request(url=self.logout_url, headers=headers)
        response = self.opener.open(request)
        result = response.read().decode('unicode_escape')
        print(result)

