import json

import requests
import jsonpath
from common.getKeyword_forResult import GetKeyword
from common.getExcel import GetExcel
from common.getExcel import GetExcels

my_time = '20240204-20240223' # *必填，迭代周期
requirementKey = 'Q00001705'
# *必填，需求文档编码
requirementKeys = ('Q00002293', 'Q00002292','Q00002291','Q00002290','Q00002289')

req_url = 'https://mgt.mysteelcms.com/dataspider-multi/api/spiderRequirement/requirementDetail/{}'.format(requirementKey)
headers = {"Cookie":"JSESSIONID=14BB3A171EF932E823AAEE115702D5C4; _login_token=d1311fd74fdf4efe936f545ca43fe8dc; _center_login_token=d1311fd74fdf4efe936f545ca43fe8dc; _last_loginaid=124e5e35196b0e0c3b47df1e1d30838f; mysteel_sso_ticket=3d5d75e9fe4e4ee5b36d0fd6d3b2de26; JSESSIONID=4DCCD47BF1201A99BD2E1C9F0559A799"}
def getRequirment():
    res = requests.request(method='get',url=req_url,headers=headers)
    res = res.json()

    requirementName = GetKeyword.get_keyword(res,'requirementName') #需求名
    tableName = GetKeyword.get_keyword(res,'tableName') #需求表名
    fieldList = res["response"]["fieldList"] #表信息对象

    fieldNames=[] #表字段名
    for field in fieldList:
        fieldNames.append(field["fieldName"])
    print(fieldNames)
    GetExcel(my_time,requirementName,tableName,fieldNames)

# def getRequirments():
#     requirementKeys = ('Q00002367','Q00002366')
#     print(len(requirementKeys))
#     for requirementKey in requirementKeys:
#         req_url = 'https://mgt.mysteelcms.com/dataspider-multi/api/spiderRequirement/requirementDetail/{}'.format(requirementKey)
#         res = requests.request(method='get', url=req_url, headers=headers)
#         res = res.json()
#
#         requirementName = GetKeyword.get_keyword(res, 'requirementName')  # 需求名
#         tableName = GetKeyword.get_keyword(res, 'tableName')  # 需求表名
#         fieldList = res["response"]["fieldList"]  # 表信息对象
#
#         fieldNames = []  # 表字段名
#         for field in fieldList:
#             fieldNames.append(field["fieldName"])
#         print(fieldNames)
#         GetExcel(my_time, requirementName, tableName, fieldNames)

def getRequirments():
    requirementNames = []  # 所有需求名称
    tableNames = []  # 所有表名
    fieldNames = []  # 所有表字段

    for requirementKey in requirementKeys:
        req_url = 'https://mgt.mysteelcms.com/dataspider-multi/api/spiderRequirement/requirementDetail/{}'.format(requirementKey)
        res = requests.request(method='get', url=req_url, headers=headers)
        res = res.json()

        requirementName = GetKeyword.get_keyword(res, 'requirementName')  # 需求名
        tableName = GetKeyword.get_keyword(res, 'tableName')  # 需求表名
        fieldList = res["response"]["fieldList"]  # 表信息对象

        fieldName = []  # 表字段名
        for field in fieldList:
            fieldName.append(field["fieldName"])
        fieldNames.append(fieldName)
        requirementNames.append(requirementName)
        tableNames.append(tableName)

    print(fieldNames)
    print(requirementNames)
    print(tableNames)
    GetExcels(my_time, requirementNames, tableNames, fieldNames)

if __name__ == '__main__':
    getRequirments()