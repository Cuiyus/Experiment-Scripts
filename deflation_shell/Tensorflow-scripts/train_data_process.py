import os, sys, re
from absl import flags
from absl import app
import pandas as pd
import xlwt
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from multiprocessing import Process
import  numpy as np

FLAGS = flags.FLAGS
flags.DEFINE_string("data_dir", ".", "数据文件存储目录")
flags.DEFINE_string("file_name", None, "处理数据目录下的某一文件")
flags.DEFINE_bool("painting", True ,"做曲线图")

def check_dir():
    if not os.path.isdir(FLAGS.data_dir):
        print("输入目录路径不存在")
        raise ValueError
    if FLAGS.file_name:
        file_path = FLAGS.data_dir + '/' + FLAGS.file_name
        if not os.path.isfile(file_path):
            print("该目录%s下不存在文件%s".format(FLAGS.data_dir, FLAGS.file_name))
            raise ValueError
        else:
            file_only = True
            return file_only
    else:
        file_only = False
        return file_only
        

def data_process(path):
    addtion_data = {}
    data = []
    table_name = []
    with open(path, '+r') as f:
        epoch_pat = re.compile("Num epochs: (.*)")
        batch_pat = re.compile("Num batches: (.*)")
        model_pat = re.compile("Model: (.*)")
        for line in f:
            model = model_pat.search(line)
            epoch = epoch_pat.search(line)
            batch = batch_pat.search(line)
            if model:
                addtion_data["model"] = model.group(1).strip()
            if epoch:
                addtion_data["epoch"] = epoch.group(1).strip()
            if batch:
                addtion_data["batch"] = batch.group(1).strip()
            if 'Img/sec' in line:
                table_name = line.split()
            if "images/sec:" in line and "total" not in line:
                train_data = line.split()
                del train_data[1], train_data[2:7] 
                data.append(train_data)
    return data,table_name,addtion_data            

def write_xls(data_pd, addtion_data, filename):
    path = 'C:\\Users\\12093\\Desktop\\Deflation\\AI\\excel'
    file_name = filename.split('.')
    p = path + '\\' + file_name[0] + '.xlsx'
    data_pd.to_excel(p, sheet_name='sheet',index=False)

def paint(data, table_name, filename):
    path = 'C:\\Users\\12093\\Desktop\\Deflation\\AI\\paint'
    file_name = filename.split('.')
    p = path + '\\' + file_name[0] + '.png'
    print(p)
    # pandas 绘图
    # paint = pd.DataFrame(data=data, index=df3['Step'], columns=table_name, dtype=np.float)
    # del paint['Step']
    # del paint['Img/sec']
    # del paint['top_5_accuracy']
    # paint.plot(kind='line')
    # plt.show()
    # print(data_pd.tail())
    # df3 = data_pd.copy()
    paint = pd.DataFrame(data=data, columns=table_name, dtype=np.float)
    plt.figure(figsize=(18, 5))
    tensor_solo = plt.plot(paint['Step'], paint['total_loss'],'b',label='Tensor-Worker')
    plt.rcParams['figure.figsize'] = (20.0, 4.0) # 设置figure_size尺寸
    # plt.title('')
    plt.xlabel('Step')
    plt.ylabel('Loss')
    plt.legend()
    # plt.show()

    plt.savefig(p)
    return 

def main(argv):
    del argv
    flag = check_dir()
    if flag:
        file_path = FLAGS.data_dir + '\\' + FLAGS.file_name
        data, table_name, addtion_data=data_process(file_path)
        data_pd = pd.DataFrame(data=data,columns=table_name)
        p_write_xls = Process(target=write_xls, args=(data_pd,addtion_data, FLAGS.file_name,))
        # write_xls(data_pd,addtion_data, FLAGS.file_name)
        p_write_xls.start()
        if FLAGS.painting:
            p_paint = Process(target=paint, args=(data, table_name,FLAGS.file_name,))
            p_paint.start()
            # paint(data_pd, FLAGS.file_name)
    else:
        file_list = os.listdir(FLAGS.data_dir)
        for f in file_list:
            file_path = FLAGS.data_dir + '\\' + f
            data, table_name, addtion_data=data_process(file_path)
            data_pd = pd.DataFrame(data=data,columns=table_name)
            write_xls(data_pd, addtion_data, f)
            if FLAGS.painting:
                paint(data, table_name, f)

if __name__ == "__main__":
    app.run(main)



