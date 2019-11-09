import xlrd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
print("输出redis -c 为30的图表")
for i in range(1,4):
    data_solo = xlrd.open_workbook("C:\\Users\\12093\\Desktop\\Deflation\\2\\solo_redis\\solo_redis_30_%d.xls" % i)
    data_colo = xlrd.open_workbook("C:\\Users\\12093\\Desktop\\Deflation\\2\\data_colocation\\co-location-30-%d.xls" % i)
    data_def = xlrd.open_workbook("C:\\Users\\12093\\Desktop\\Deflation\\2\\colocat_deflation\\deflation-30-%d.xls" % i)

    table_solo = data_solo.sheets()[0]
    table_colo = data_colo.sheets()[0]
    table_def = data_def.sheets()[0]

    y_solo = table_solo.col_values(0)
    y_colo = table_colo.col_values(0)
    y_def = table_def.col_values(0)

    # x = np.arange(len(y_def))
    x_solo = range(len(y_solo))
    x_colo = range(len(y_colo))
    x_def = range(len(y_def))

    # 设置输出图片的尺寸
    plt.figure(figsize=(18, 5))

    l_solo = plt.plot(x_solo, y_solo, 'r', label='solo_redis_30_3')
    l_colo = plt.plot(x_colo, y_colo, 'g', label='colo_30_3')
    l_def = plt.plot(x_def, y_def, 'b', label='def_30_3')


    plt.rcParams['figure.figsize'] = (20.0, 4.0) # 设置figure_size尺寸
    plt.title('Deflation Compare')
    plt.xlabel('Time/s')
    plt.ylabel('QPS')
    plt.legend()
    # plt.show()
    plt.savefig("C:\\Users\\12093\\Desktop\\Deflation\\2\\数据分析\\30-%d.jpg" % i)
print("输出redis -c 为20的图表")
for i in range(1,4):
    data_solo = xlrd.open_workbook("C:\\Users\\12093\\Desktop\\Deflation\\2\\solo_redis\\solo_redis_25_%d.xls" % i)
    data_colo = xlrd.open_workbook("C:\\Users\\12093\\Desktop\\Deflation\\2\\data_colocation\\co-location-25-%d.xls" % i)
    data_def = xlrd.open_workbook("C:\\Users\\12093\\Desktop\\Deflation\\2\colocat_deflation\\deflation-25-%d.xls" % i)

    table_solo = data_solo.sheets()[0]
    table_colo = data_colo.sheets()[0]
    table_def = data_def.sheets()[0]

    y_solo = table_solo.col_values(0)
    y_colo = table_colo.col_values(0)
    y_def = table_def.col_values(0)

    # x = np.arange(len(y_def))
    x_solo = range(len(y_solo))
    x_colo = range(len(y_colo))
    x_def = range(len(y_def))

    # 设置输出图片的尺寸
    plt.figure(figsize=(18, 5))

    l_solo = plt.plot(x_solo, y_solo, 'r', label='solo_redis_25_3')
    l_colo = plt.plot(x_colo, y_colo, 'g', label='colo_25_3')
    l_def = plt.plot(x_def, y_def, 'b', label='def_25_3')


    plt.rcParams['figure.figsize'] = (20.0, 4.0) # 设置figure_size尺寸
    plt.title('Deflation Compare')
    plt.xlabel('Time/s')
    plt.ylabel('QPS')
    plt.legend()
    # plt.show()
    plt.savefig("C:\\Users\\12093\\Desktop\\Deflation\\2\\数据分析\\25-%d.jpg" % i)