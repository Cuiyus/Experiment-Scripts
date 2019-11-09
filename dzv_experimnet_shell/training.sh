#!/bin/bash 
# Note
# 运行脚本需保证在容器内存在文件 -run.sh-
# 如果要更改实验内容需要修改 -run.sh-文件

kubectl exec -it tensorflow-ps-rc-gpu-85cn4 -c ps-gpu -n dzv -- bash /tf/run.sh &

echo "开始数据采集"
# 这里多进程的等待问题没办法解决
# 使用人为采集（开启脚本）
wait
echo "执行采集结束操作"

# 将于nvidia有关的进程号保存到变量pid_array_str
pid_array_str=$(ps aux | grep nvidia-smi | grep -v grep | awk '{print $2}') 
# 变量pid_array_str转换数组
pid_array_int=(${array//,/})

len=${#pid_array_int[*]}

for ((i=0;i<"${len}";i++));
do
kill -9 ${pid_array_int[i]} &
done
wait
echo "采集结束"








