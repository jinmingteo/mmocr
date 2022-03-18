#!/usr/bin/env bash

if [ $# -lt 3 ]
then
    echo "Usage: bash $0 CONFIG WORK_DIR GPUS"
    exit
fi

CONFIG=$1
WORK_DIR=$2
GPUS=$3

PORT=${PORT:-29500}

PYTHONPATH="$(dirname $0)/..":$PYTHONPATH \

if [ ${GPUS} == 1 ]; then
    python tools/train.py  $CONFIG --work-dir=${WORK_DIR} ${@:4}
else
    CUDA_VISIBLE_DEVICES=1,3 python -m torch.distributed.launch --nproc_per_node=$GPUS --master_port=$PORT \
        tools/train.py $CONFIG --work-dir=${WORK_DIR} --launcher pytorch ${@:4}
fi
