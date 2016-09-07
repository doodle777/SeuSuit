# -*= coding:utf-8 -*-

from http import cookiejar
from urllib import request as Req
from urllib import parse
import re



class Grade:
    def __init__(self):
        self.userID = '151538'
        self.password = '19930830'
        self.login_url = 'http://202.119.4.150/nstudent/login.aspx'
        self.grade_url = 'http://202.119.4.150/nstudent/grgl/xskccjcx.aspx'
        self.cookies = cookiejar.CookieJar()
        self.opener = Req.build_opener(Req.HTTPCookieProcessor(self.cookies))

    def login(self):
        # 获取 __VIEWSTATE
        request = Req.Request(self.login_url)
        response = self.opener.open(request)
        reg_viewstate = re.compile('VIEWSTATE".*?value="(.*?)" />', re.S)
        viewstate = reg_viewstate.search(response.read().decode('utf-8'))

        if viewstate is not None:
            viewstate = viewstate.group(1)
        else:
            print("No VIEWSTATE found!")

        login_data = parse.urlencode({
            '__VIEWSTATE':  viewstate,
            'txt_user':     self.userID,
            'txt_password': self.password,
            'ok.x':         '25',
            'ok.y':         '11'
        }).encode('ascii')

        login_headers = {
            'Accept':           'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Ecoding':   'gzip, deflate',
            'Accept-Language':  'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control':    'max-age=0',
            'Connection':       'keep-alive',
            # 'Content-Length':   '126',
            'Content-Type':     'application/x-www-form-urlencoded',
            # 'Cookie':           'ASP.NET_SessionId=bi0p2y45h05p4evtewbx4245',
            'DNT':              '1',
            'Host':             '202.119.4.150',
            'Origin':           'http://202.119.4.150',
            'Referer':          'http://202.119.4.150/nstudent/login.aspx',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent':       'Chrome/52.0.2743.116 Safari/537.36',
        }

        request = Req.Request(url=self.login_url, data=login_data, headers=login_headers)
        response = self.opener.open(request)
        # print(response.read().decode('utf-8'))

    def logout(self):
        # 获取 __VIEWSTATE
        request = Req.Request(self.login_url)
        response = self.opener.open(request)
        reg_viewstate = re.compile('VIEWSTATE".*?value="(.*?)" />', re.S)
        viewstate = reg_viewstate.search(response.read().decode('utf-8'))

        logout_data = parse.urlencode({
            '__VIEWSTATE': viewstate,
            'Button2': '退出登录'
        }).encode('ascii')

        logout_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Ecoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Content-Length':   '126',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie':           'ASP.NET_SessionId=bi0p2y45h05p4evtewbx4245',
            'DNT': '1',
            'Host': '202.119.4.150',
            'Origin': 'http://202.119.4.150',
            'Referer': 'http://202.119.4.150/nstudent/login.aspx',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Chrome/52.0.2743.116 Safari/537.36',
        }

        request = Req.Request(url=self.login_url, data=logout_data, headers=logout_headers)
        response = self.opener.open(request)
        print(response.read().decode('utf-8'))

    def get_grade(self):
        request = Req.Request(self.grade_url)
        response = self.opener.open(request).read().decode('utf-8')
        # print(response)

        reg_id       = re.compile('id="lblxm"><b>(.*?)</b>', re.S)
        reg_name     = re.compile('id="lblxh"><b>(.*?)</b>', re.S)
        reg_normal   = re.compile('id="lblgghpjcj">(.*?)</span></td>', re.S)
        reg_info     = re.compile('id="lblzt".*?"3">(.*?)</font></span></P>', re.S)
        reg_required = re.compile('id="dgData"(.*?)</table></td>', re.S)
        reg_elective = re.compile('id="Datagrid1"(.*?)</table></td>', re.S)
        reg_item     = re.compile('<td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>', re.S)

        id        = reg_id.search(response).group(1)
        name      = reg_name.search(response).group(1)
        normalize = reg_normal.search(response).group(1)
        info      = reg_info.search(response).group(1)
        required  = reg_required.search(response).group(1)
        elective  = reg_elective.search(response).group(1)
        item_req  = reg_item.findall(required)
        item_ele  = reg_item.findall(elective)

        print(id, name, normalize)
        for item in item_req:
            print(item)
        print('-------------------------')
        for item in item_ele:
            print(item)
        print(info)


grade = Grade()
grade.login()
grade.get_grade()
# grade.logout()
