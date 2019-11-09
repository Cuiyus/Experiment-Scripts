#!/bin/bash
export exper_path=/home/tank/k8s/dzv
exper_data="${exper_path}/data"

if [ ! -d "${exper_data}" ];
then
    mkdir -p "${exper_data}"
fi
echo "信息输入到${exper_data}"

nvidia-smi dmon >> "${exper_data}/dmon.log" 2>&1 &
nvidia-smi dmon -s m >> "${exper_data}/dmon_m.log" 2>&1 &
nvidia-smi dmon -s t >> "${exper_data}/dmon_t.log" 2>&1 &
