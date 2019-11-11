#!/bin/bash 
DATA_PATH=/home/tank-cys/deflation/solo_redis
echo "------------------Starting  Redis-bench -c 25-------------------"
for((i=1;i<=3;i++))
do
	docker exec -i Redis-bench /root/redis-cluster-bench -h 192.168.1.160 -p 6379 -n 10000000 -c 25 -t set,get --interval 1 >> ${DATA_PATH}/solo_redis_25_${i}.txt
done 
echo "------------------Starting  Redis-bench -c 30-------------------"
for((i=1;i<=3;i++))
do
        docker exec -i Redis-bench /root/redis-cluster-bench -h 192.168.1.160 -p 6379 -n 10000000 -c 30 -t set,get --interval 1 >> ${DATA_PATH}/solo_redis_30_${i}.txt
done
