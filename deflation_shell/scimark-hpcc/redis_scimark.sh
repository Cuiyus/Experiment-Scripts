#!/bin/bash
DATA_PATH=/home/tank-cys/deflation/scimark/data
redis_bench_id=$(docker exec -i Redis-bench ps aux |grep redis* | grep -v grep | awk '{print $2}') 
stat=$1
echo "Start co-location redis and scimark"
if [[ ${stat} == "start" ]]
then
	for ((i=1;i<=6;i++))
	do
		echo "${i}"
		# docker exec -i Scimark /root/scimark/run.sh >> ${DATA_PATH}/scimark${i}.txt &
		docker exec -i Redis-bench /root/redis-cluster-bench -h 192.168.1.160 -p 6379 -n 10000000 -c 30 -t set,get --interval 1 >> ${DATA_PATH}/redis-30-${i}.txt &
		docker exec -i Scimark /root/scimark/run.sh >> ${DATA_PATH}/scimark-30-${i}.txt 
	wait 
	done
elif [[ ${stat} == "stop" ]]
then 
	# echo "stop scimark"
	docker exec -i Scimark /bin/bash /root/scimark/stop-scimark.sh
	echo "stop scimark"
	docker exec -i Redis-bench kill -9 ${redis_bench_id} 
	echo "stop redis"
fi
