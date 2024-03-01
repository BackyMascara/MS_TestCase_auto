import requests
from common.getKeyword_forResult import GetKeyword
from common.getExcel import GetExcel
from common.getExcel import GetExcels

# *必填my_time，迭代周期
my_time = '20240226-20240308'
requirementKey = 'Q00001705'
# *必填requirementKeys，需求文档编码
requirementKeys = ('Q00002528', 'Q00002525','Q00002523','Q00002522','Q00002521','Q00002520','Q00002510','Q00002501','Q00002497','Q00002480','Q00002470','Q00002461','Q00002457','Q00002456','Q00002450','Q00002429','Q00002426','Q00002425','Q00002401','Q00002396','Q00002390','Q00002389','Q00002388','Q00002387','Q00002385','Q00002374','Q00002373','Q00002362','Q00002370')
req_url = 'https://mgt.mysteelcms.com/dataspider-multi/api/spiderRequirement/requirementDetail/{}'.format(requirementKey)
# *必填，Cookie
headers = {"Cookie":"JSESSIONID=E99332FE3B53EDF95A9967BC1BE470E7; _login_token=db65df3bec6a45d78254284f8386b019; _center_login_token=db65df3bec6a45d78254284f8386b019; _last_loginaid=4a4cab8a25323d3d2e03363b2d0ad413; mysteel_sso_ticket=aebebf506e6a48048f3bc278e3b91e0d; JSESSIONID=D54A9E367364E4188ED1551CE9E16D55"}
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