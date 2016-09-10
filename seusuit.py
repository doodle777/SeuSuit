#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import SeuSuit.Network.login as Login
import SeuSuit.Academic.grade as Grade


def read_cfg():
    cfg = open('config.ini')
    infos = cfg.readlines()
    map = {}

    for info in infos:
        key = info.split('=')[0].strip()
        val = info.split('=')[1].strip()
        # print(key, val)
        map[key] = val

    return map


def read_args():
    args = sys.argv
    argc = len(sys.argv)

    service = ''
    user_name = ''
    password = ''

    if argc <= 1 or (argc != 2 and argc != 4):
        print('USAGE: python seusuit.py serviceName [userName, [password]]')
    elif argc == 2:
        service = args[1]
    elif argc == 4:
        service = args[1]
        user_name = args[2]
        password = args[3]

    return service, user_name, password


def start():
    cfg = read_cfg()
    service, user_name, password = read_args()
    # print(cfg)
    # print(service, user_name, password)

    if service == 'login':
        if user_name == '' or password == '':
            user_name = cfg['network_username']
            password = cfg['network_password']
            login = Login.Login(user_name, password)
            login.login()

    if service == 'logout':
        login = Login.Login(user_name, password)
        login.logout()

    if service == 'checkgrade':
        if user_name == '' or password == '':
            user_name = cfg['academic_username']
            password = cfg['academic_password']
            grade = Grade.Grade(user_name, password)
            grade.login()
            grade.get_grade()
            grade.logout()

# print(read_cfg())
start()

