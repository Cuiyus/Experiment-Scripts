#!/bin/bash
DATA_PATH=/home/tank-cys/deflation/colocat_deflation
echo "---------------------Start Experiment Co-location -25------------------------"
for ((i=1;i<=3;i++))
do
        docker exec -i Spark-1 /bin/bash /root/sparkbench/spark-bench-legacy/KMeans/bin/run_java.sh >> /dev/null &
        sleep 5
        docker exec -i Redis-bench /root/redis-cluster-bench -h 192.168.1.160 -p 6379 -n 10000000 -c 25 -t set --interval 1 >>  $DATA_PATH/deflation-25-${i}.txt &
        echo "开始轮询"
        tag=1
        n=10
        while true
        do
            exectur_pid=$(docker exec -i Spark-5 /usr/local/jdk1.8.0/bin/jps | grep CoarseGrainedExecutorBackend | grep -v grep | awk '{print $1}')
            if [[ "${exectur_pid}" ]]
            then
                if [[ ${tag}==1 ]]
                then
                        sleep 10
                        echo "Resource Deflation:KILL CoarseGrainedExecutorBackend"
                        docker exec -i Spark-5 kill -9 ${exectur_pid}
                        tag=0
                        let n=n-1
                        echo "Exectuor 资源已释放"
                else
                        echo "Resource Deflation:KILL CoarseGrainedExecutorBackend"
                        docker exec -i Spark-5 kill -9 ${exectur_pid}
                        let n=n-1
                        echo "Exectuor 资源已释放"
                fi
            else
                sleep 10
                let n=n-1
            fi
            if [[ ${n} == 0]]
            then
                  echo "停止轮询"
                  break
            fi
        done
wait
done


echo "---------------------Start Experiment Co-location -30------------------------" 
for ((i=1;i<=3;i++))
do
        docker exec -i Spark-1 /bin/bash /root/sparkbench/spark-bench-legacy/KMeans/bin/run_java.sh >> /dev/null &
        sleep 5
        docker exec -i Redis-bench /root/redis-cluster-bench -h 192.168.1.160 -p 6379 -n 10000000 -c 30 -t set --interval 1 >>  $DATA_PATH/deflation-30-${i}.txt &
        echo "开始轮询"
        tag=1
        n=10
        while true
        do
            exectur_pid=$(docker exec -i Spark-5 /usr/local/jdk1.8.0/bin/jps | grep CoarseGrainedExecutorBackend | grep -v grep | awk '{print $1}')
            if [[ "${exectur_pid}" ]]
            then
                if [[ ${tag}==1 ]]
                then
                        sleep 10
                        echo "Resource Deflation:KILL CoarseGrainedExecutorBackend"
                        docker exec -i Spark-5 kill -9 ${exectur_pid}
                        tag=0
                        let n=n-1
                        echo "Exectuor 资源已释放"
                else
                        echo "Resource Deflation:KILL CoarseGrainedExecutorBackend"
                        docker exec -i Spark-5 kill -9 ${exectur_pid}
                        let n=n-1
                        echo "Exectuor 资源已释放"
                fi
            else
                sleep 10
                let n=n-1
            fi
            if [[ ${n} == 0]]
            then
                  echo "停止轮询"
                  break
            fi
        done
wait
done
echo "----------------------------------End Experiment------------------------------"
