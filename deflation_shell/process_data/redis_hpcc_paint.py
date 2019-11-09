import xlrd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
for i in range(1,7):
    data_colo = xlrd.open_workbook("C:\\Users\\12093\\Desktop\\Deflation\\科学计算\\hpcc\\data\\redis-30-%d.xls" % i)
    table_colo = data_colo.sheets()[0]
    y_colo = table_colo.col_values(0)
    x_colo = range(len(y_colo))

    # 设置输出图片的尺寸
    plt.figure(figsize=(18, 5))
    l_colo = plt.plot(x_colo, y_colo, 'g', label='redis_hpcc')

    plt.rcParams['figure.figsize'] = (20.0, 4.0) # 设置figure_size尺寸
    plt.title('Deflation Compare')
    plt.xlabel('Time/s')
    plt.ylabel('QPS')
    plt.legend()
    # plt.show()
    plt.savefig("C:\\Users\\12093\\Desktop\\Deflation\\科学计算\\hpcc\\data\\redis-%d.jpg" % i)
