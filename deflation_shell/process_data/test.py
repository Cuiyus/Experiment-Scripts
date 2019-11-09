import xlrd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
for i in range(1,7):
    data_hpcc = xlrd.open_workbook("C:\\Users\\12093\\Desktop\\Deflation\\科学计算\\hpcc\\data\\redis-30-%d.xls" % i)
    table_hpcc = data_hpcc.sheets()[0]
    y_hpcc = table_hpcc.col_values(0)
    x_hpcc = range(len(y_hpcc))

    data_scimark = xlrd.open_workbook("C:\\Users\\12093\\Desktop\\Deflation\\科学计算\\scimark\\data\\redis%d.xls" % i)
    table_scimark = data_scimark.sheets()[0]
    y_scimark = table_scimark.col_values(0)
    x_scimark = range(len(y_scimark))

    # 设置输出图片的尺寸
    plt.figure(figsize=(18, 5))
    l_hpcc = plt.plot(x_hpcc, y_hpcc, 'g', label='redis_hpcc')
    l_scimark = plt.plot(x_scimark, y_scimark, 'b', label='redis_scimark')
    plt.rcParams['figure.figsize'] = (20.0, 4.0) # 设置figure_size尺寸
    plt.title('Deflation Compare')
    plt.xlabel('Time/s')
    plt.ylabel('QPS')
    plt.legend()
    # plt.show()
    plt.savefig("C:\\Users\\12093\\Desktop\\Deflation\\科学计算\\hpcc\\compare-%d.jpg" % i)

