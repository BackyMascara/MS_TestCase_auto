import json

import requests
import jsonpath
from common.getKeyword_forResult import GetKeyword
from common.getExcel import GetExcel

my_time = '20240204-20240223'
requirementKey = 'Q00001705'

req_url = 'https://mgt.mysteelcms.com/dataspider-multi/api/spiderRequirement/requirementDetail/{}'.format(requirementKey)
headers = {"Cookie":"JSESSIONID=CA6C111F48639C7C012A6493A8F4B064; JSESSIONID=A2F1ACA6EB5BF9DBC9FAEF22D58CCC05; _center_login_token=45d381375eb548199fceebc587c1877d; _login_token=45d381375eb548199fceebc587c1877d; _last_loginaid=c541c265c13f5644a79cc193f9a8065e; mysteel_sso_ticket=9a1809cc66984abab996ce364138c19e; buriedDistinctId=412baa16e5c34c799f42274224928fb3; BURIED_STROAGE.mysteelcms.com=eyJTRUVTSU9OSUQiOiI0MzBiMmMzMjM1ZmU1NTM2IiwiU0VFU0lPTkRBVEUiOjE3MDcwOTc5NDA2OTUsIkFOU0FQUElEIjoiIiwiQU5TJERFQlVHIjowLCJBTlNVUExPQURVUkwiOiIvL3N0YXRzLm15c3RlZWwuY29tIiwiRlJJU1REQVkiOiIyMDIzMDgwMSJ9"}
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

if __name__ == '__main__':
    getRequirment()