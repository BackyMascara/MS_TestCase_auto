from openpyxl import load_workbook

def GetExcel(my_time,requirementNames,tableNames,fieldNames):

    # 打开现有的模板Excel文件
    wb = load_workbook(r'E:\测试用例-fl\爬虫\20240204-20240223\测试用例-自动.xlsx')

    # 选择要操作的工作表（默认为第一个）
    ws = wb.active
    i = 2 #测试用例名称的单元格位置
    j = 4 #测试步骤的单元格位置
    TC_name_index = 'A' + str(i)  # 用例名称
    TC_module_index = 'B' + str(i)  # 所属模块
    # 设置要写入的单元格位置及值
    ws[TC_name_index] = '检查“ ' + requirementNames + ' ”需求数据'
    ws[TC_module_index] = '/' + my_time + '/' + requirementNames + ' ( ' + tableNames + ' )'

    # 前两行固定写死
    ws['C2'] = '数据准确性'
    ws['D2'] = '与原网站数据一致'
    ws['C3'] = '与原网站数据一致'
    ws['D3'] = '与原网站数据一致'

    for fieldName in fieldNames:
        TC_step_index = 'C' + str(j)  # 步骤描述
        TC_result_index = 'D' + str(j)  # 预期结果

        #第3行
        ws[TC_step_index] = '检查mysteel_spider.' + tableNames + ' 表 ' + fieldName + ' 字段数据'
        ws[TC_result_index] = '符合前置需求文档字段清洗逻辑和质检逻辑'

        j = j + 1

    # 保存修改并关闭Excel文件
    save_url = r'E:\测试用例-fl\爬虫\{}\测试用例-{}.xlsx'.format(my_time,tableNames)
    wb.save(save_url)
    wb.close()

if __name__ == '__main__':
    my_time = '20240204-20240223'
    fieldNames = ['data_date', 'breed_name', 'maturity_num', 'maturity_num_1m', 'maturity_num_2m', 'remark']
    requirementNames = '上海期货交易所标准仓单到期数量'
    tableNames = 'fu_spi_wh_maturity_num'
    GetExcel(my_time,requirementNames,tableNames,fieldNames)