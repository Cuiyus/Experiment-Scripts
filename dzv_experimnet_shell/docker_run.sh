#!/bin/bash
export TF_CNN_Benchmark=/tf/benchmarks-master/scripts/tf_cnn_benchmarks

logdir="${TF_CNN_Benchmark}/log"
log="${logdir}/experiment.log"
echo "Training Start **日志输出到${log}"
if [ ! -d "${logdir}" ];
then
        mkdir "${logdir}"
        CUDA_VISIBLE_DEVICES=0 python $TF_CNN_Benchmark/tf_cnn_benchmarks.py --data_format=NCHW --batch_size=32 --model=vgg11 --num_gpus=1 > "${log}" 2>&1
        if [ $? -ne 0 ];then
                echo "Error: failed to run command "
                exit 1
        fi
else
        CUDA_VISIBLE_DEVICES=0 python $TF_CNN_Benchmark/tf_cnn_benchmarks.py --data_format=NCHW --batch_size=32 --model=vgg11 --num_gpus=1 > "${log}" 2>&1
        if [ $? -ne 0 ];then
                echo "Error: failed to run command "
                exit 2
        fi
fi
echo "Training End"
                         