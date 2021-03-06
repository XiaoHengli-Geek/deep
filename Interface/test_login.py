from Public.log import logger,LOG
import os
import requests
import json
import ddt
import unittest
from Public.read_excel import read_excel
from Public.db_commit import db_commit
from Public.cogfig import EXECL_PATH
import random
from Interface.test_login_request import requests_login_packge
wenjian = EXECL_PATH + '\\jekn.xlsx'  #查询到对应的case文件
excel = read_excel(wenjian,'Sheet2')
db_link=db_commit()

class Test_Login(object):
    def __init__(self,canshu1):
        self.canshu1=canshu1
    def test_sql(self):
        sql = "SELECT * FROM `user` WHERE uid in ('%s')"%(self.canshu1)
        name = db_link.get_all(sql)
        phone = []

        for i in range(0, 1):
            print('')
            phone.append(name[i]['phone'])
        return phone
    def test_log(self):
        sql_phone=self.test_sql()
        print(type(sql_phone))
        token1 = {"token": [], "contract_type": []}
        tokenList = []
        contract_typeList = []
        url='https://t01-mapi.deepcoin.pro/site/new-login'
        for i in sql_phone:
            api = requests_login_packge(url=url, requersts_type='post', mobile=i, code='1234')
            try:

                login_api_json = api.getJson()
                # token = {"token": api_json.get('retData').get('token'), "retMsg": api_json.get('retMsg')}
                print(login_api_json)
                tokenList.append(login_api_json.get('retData').get('token'))
                print(login_api_json.get('retData')['user']['contract_type'])
                contract_typeList.append(login_api_json.get('retData')['user']['contract_type'])
                print(login_api_json.get('retData')['user']['contract_type'])
                retMsg = login_api_json.get('retMsg')
                print(retMsg)
                print(contract_typeList)
            except Exception as e:
                print(e)
            finally:
                print('结束')
                # return dict(token1)
        token1["token"] = tokenList
        token1["contract_type"] = contract_typeList
        return token1

# test = Test_Login('316173')
# token_test = test.test_log()