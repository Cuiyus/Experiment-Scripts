#!/bin/bash
echo "Stop-Redis-bench"
redis_bench_id=$(docker exec -i Redis-bench ps aux |grep redis* | grep -v grep | awk '{print $2}')
if [[ ${redis_bench_id} ]]
then
	docker exec -i Redis-bench kill -9 ${redis_bench_id}
else
	echo "redis-bench未启动"
fi

echo "Stop-Spark"
app_id=$(docker exec -i Spark-1 /root/hadoop/hadoop2.7.7/bin/yarn application -list 2>/dev/null | grep -v grep | awk '{print $1}'| grep application*)
if [[ ${app_id} ]]
then
	echo "application_id ${app_id}"
	docker exec -i Spark-1 /root/hadoop/hadoop2.7.7/bin/yarn application -kill ${app_id}
	echo "application killde"
else
	echo "该节点未运行spark任务"
fi
echo "Stoped Spark"
