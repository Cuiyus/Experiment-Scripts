import sys
import os
import re
import xlwt
# import pandas as pd
import xlwt, xlrd
from xlutils.copy import copy


def default_process():
    if (len(sys.argv) == 3):
        path = sys.argv[1]
        filename = sys.argv[2]
    elif (len(sys.argv) == 2):
        if (sign in sys.argv[1] for sign in ['/', '\\']):
            path = sys.argv[1]
            filename = 'All'
        else:
            path = './'
            filename = sys.argv[1]
    else:
        path = './'
        filename = 'All'

    return path, filename


def write_file(filepath, filename, mode='r'):
    if filename == 'All':
        listdir = os.listdir(filepath)
        print(listdir)
        for name in listdir:
            # if name == '...': continue
            process_file(filepath, name)
    else:
        process_file(filepath, filename)
    return


def write_txt(filename, data, data_header):
    with open(filename, 'a+') as w:
        for key in data.keys():
            data_line = ' '.join(data[key])
            data_line = data_header + ' ' + key + ' ' + data_line

        w.writelines([data_line, '\n'])
        w.flush()


def write_excel_xls(path, data, tablename, sec, opcs, avg_opc):
    # index = len(value)  # 获取需要写入数据的行数
    # print('1')
    workbook = xlwt.Workbook()  # 新建一个工作簿
    # sheet_name = []
    for key in data.keys():
        name = key
        # sheet_name.append(name)
        sheet = workbook.add_sheet(name)  # 在工作簿中新建一个表格
        for i, n in enumerate(tablename):
            sheet.write(0, i , n)

        sheet.write(1, 0, sec)
        sheet.write(1, 1, opcs)
        sheet.write(1, 2, avg_opc)

        for i in range(len(data[key])):
            sheet.write(1, i + 3, data[key][i])
    workbook.save(path)  # 保存工作簿
    # print("xls格式表格写入数据成功！")


def write_excel_xls_append(path, data, tablename, sec, opcs, avg_opc):
    # index = len(value)  # 获取需要写入数据的行数

    # print(sheets)
    for key in data.keys():
        workbook = xlrd.open_workbook(path)  # 打开工作簿
        sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
        if key not in sheets:
            # print(key)
            new_workbook = copy(workbook)
            # new_worksheet = new_workbook.add_sheet(key)

            sheet = new_workbook.add_sheet(key)
            for i, n in enumerate(tablename):
                sheet.write(0, i, n)

            sheet.write(1, 0, sec)
            sheet.write(1, 1, opcs)
            sheet.write(1, 2, avg_opc)

            for i in range(len(data[key])):
                sheet.write(1, i + 3, data[key][i])

            new_workbook.save(path)
        else:
            # print("1")
            # print(key)
            worksheet = workbook.sheet_by_name(key)
            rows_old = worksheet.nrows
            new_workbook = copy(workbook)
            new_worksheet = new_workbook.get_sheet(key)

            new_worksheet.write(rows_old, 0, sec)
            new_worksheet.write(rows_old, 1, opcs)
            new_worksheet.write(rows_old, 2, avg_opc)

            for i in range(len(data[key])):
                new_worksheet.write(rows_old, i + 3, data[key][i])
            new_workbook.save(path)
            # print("xls格式表格【追加】写入数据成功！")


def process_file(filepath, filename):
    # print("filepath : %s\nfilename : %s" % (filepath, filename))
    with open(filepath + filename, 'r') as f:
        # print('1')
        flag = 0  # excel第一次写入标志位

        for line in f:
            # print('2',line)
            if (line.find('Command line') != -1):
                # print('3', line)
                DB_pat = re.compile('com\.yahoo\.ycsb\.db\.(.*)Client')
                Thread_pat = re.compile('workloads/workload(.) -s -threads (.*) -t')
                mbj1 = DB_pat.search(line)
                mbj2 = Thread_pat.search(line)
                if mbj1 and mbj2:
                    wname = mbj1.group(1)
                    postx_txt = ".%s.%s.txt" % (mbj2.group(1), mbj2.group(2))
                    postx_xls = ".%s.%s.xls" % (mbj2.group(1), mbj2.group(2))
                # print(wname+postx_xls)
            elif 'wname' and 'postx_txt' in locals().keys():
                opc_pat = re.compile('\[([^\[\]]*)?\]')
                list_opc = opc_pat.findall(line)
                # print(line, len(list_opc), list_opc)
                if len(list_opc) > 1:
                    sec_pat = re.compile(' ([^ ]*) sec:')
                    pat_opc = re.compile('sec: (.*) operations; (.*) current ops/sec;')

                    sec = sec_pat.search(line).group(1)
                    opcs = pat_opc.search(line).group(1)
                    avg_opc = pat_opc.search(line).group(2)

                    data = {}

                    for i in range(len(list_opc)):
                        opc = list_opc[i].split()
                        opc_name = opc[0][:-1]
                        opc_count = opc[1][6:-1]
                        opc_maxL = opc[2][4:-1]
                        opc_minL = opc[3][4:-1]
                        opc_avg = opc[4][4:-1]
                        opc_90 = opc[5][3:-1]
                        opc_99 = opc[6][3:-1]
                        opc_999 = opc[7][5:-1]
                        opc_9999 = opc[8][6:]

                        data[opc_name] = [opc_count, opc_maxL,
                                          opc_minL, opc_avg,
                                          opc_90, opc_99, opc_999, opc_9999]



                    data_header = ' '.join([sec, opcs, avg_opc])

                    tablename = ['SEC(m)', 'TOTAL_OPC', 'QPS(ops/sec)', 'OPC_COUNT', 'OPC_MAXL(us)',
                                 'OPC_MINL(us)','OPC_AVG', '90%(us)', '99%(us)', '99.9%(us)', '99.99%(us)']

                    #  去掉注释 输出txt文件
                    #  write_txt(wname+postx_txt, data, data_header)

                    if flag == 0:
                        # print("1")
                        # print(avg_opc)
                        write_excel_xls(wname + postx_xls, data, tablename, sec, opcs, avg_opc)
                        # print("2")
                        flag = 1
                    else:
                        write_excel_xls_append(wname + postx_xls, data, tablename, sec, opcs, avg_opc)

            else:
                continue



if __name__ == '__main__':
    filepath, filename = default_process()
    print("filepath : %s\nfilename : %s" % (filepath, filename))
    # print(filepath,filename)
    write_file(filepath, filename)

