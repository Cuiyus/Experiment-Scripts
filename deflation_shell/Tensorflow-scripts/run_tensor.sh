#!/bin/bash
echo "Set env"
docker exec -e CUDA_VISIBLE_DEVICES=-1 Tensor-PS bash
docker exec -e CUDA_VISIBLE_DEVICES=-1 Tensor-Worker-1 bash
docker exec -e CUDA_VISIBLE_DEVICES=-1 Tensor-Worker-2 bash

ps_pid=$(docker exec -i Tensor-PS ps aux|grep python|grep -v grep|awk '{print $2}')
if [[ $ps_pid ]]
then
    echo "PS has exited"
else
    echo "Start PS"
    docker exec -i Tensor-PS python /root/benchmarks-master/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --data_format=NHWC --batch_size=16 --model=lenet --print_training_accuracy=True --num_batches=2000 --job_name=ps --ps_hosts=172.17.0.11:8888 --worker_hosts=172.17.0.12:8888,172.17.0.13:8888 --task_index=0 >> /dev/null 2>&1 &
fi 
echo "Start Work-1"
docker exec -i Tensor-Worker-1 python /root/benchmarks-master/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --data_format=NHWC --batch_size=16 --model=lenet --print_training_accuracy=True --num_batches=2000 --job_name=worker --ps_hosts=172.17.0.11:8888 --worker_hosts=172.17.0.12:8888,172.17.0.13:8888 --task_index=0 >> /dev/null 2>&1 &
echo "Start Work-2"
docker exec -i Tensor-Worker-2 python /root/benchmarks-master/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --data_format=NHWC --batch_size=16 --model=lenet --print_training_accuracy=True --num_batches=2000 --job_name=worker --ps_hosts=172.17.0.11:8888 --worker_hosts=172.17.0.12:8888,172.17.0.13:8888 --task_index=1 >> /dev/null 2>&1 &

