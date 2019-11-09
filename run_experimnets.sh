#! /bin/bash

# Information
# sh run_experiment.sh [basic database] [workload] [threads]
# basic-database: mongodb-async cassandra-cql 
# workload: a  / b

PYTHON="/usr/bin/python3.4" 
export YCSB_CASSANDRA=/home/tank/l_cys/ycsb-mongodb-binding-0.15.0


OUTPUT_PATH="${YCSB_CASSANDRA}/data"
WORKLOAD_PATH="${YCSB_CASSANDRA}/workloads"


basicDB=$1
shift
tem=$1
shift 

if [  ! $1 ];
then
	n=0
	while [ $n -le 80 ]
	do 
		let n=n+4
		
		${YCSB_CASSANDRA}/bin/ycsb run ${basicDB} -P ${WORKLOAD_PATH}/workload${tem} -s -threads ${n} > ${OUTPUT_PATH}/Loadtest.${n}.txt  2>&1	
		if [ $? -ne 0 ]; then
			echo "ERROR:Failed to run command"
			exit 1
		fi	
	done
else
	n=$1
	${YCSB_CASSANDRA}/bin/ycsb run ${basicDB} -P ${WORKLOAD_PATH}/workload${tem} -s -threads ${n} > ${OUTPUT_PATH}/Loadtest.${n}.txt  2>&1
        if [ $? -ne 0 ]; then
            	echo "ERROR:Failed to run command"
                exit 1
        fi
fi 

# python  
