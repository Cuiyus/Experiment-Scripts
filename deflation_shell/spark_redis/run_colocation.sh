#!/bin/bash

num_experiments=3
DATA_PATH=/home/tank-cys/deflation/data_colocation
exectur_pid=$(jps | grep Coarse* | grep -v grep | awk '{print $1}')
echo "---------------------Start Experiment Co-location -25------------------------"
for ((i=1;i<=3;i++))
do 
	docker exec -i Spark-1 /bin/bash /root/sparkbench/spark-bench-legacy/KMeans/bin/run_java.sh & 
	docker exec -i Redis-bench /root/redis-cluster-bench -h 192.168.1.160 -p 6379 -n 10000000 -c 25 -t set,get --interval 1 >>  $DATA_PATH/co-location-25-${i}.txt &
wait
done
 
echo "---------------------Start Experiment Co-location -30------------------------" 
for ((i=1;i<=3;i++))
do
        docker exec -i Spark-1 /bin/bash /root/sparkbench/spark-bench-legacy/KMeans/bin/run_java.sh &
        docker exec -i Redis-bench /root/redis-cluster-bench -h 192.168.1.160 -p 6379 -n 10000000 -c 30 -t set,get --interval 1 >>  $DATA_PATH/co-location-30-${i}.txt &
wait
done
echo "----------------------------------End Experiment------------------------------"
