#!/bin/bash
if [ ! $# -eq 1 ] ; then
    echo "Usage : ./dump.sh timestamp'"
    exit 1
fi
STRUCT_FILE="struct_'echo $1'.sql "
DATA_FILE="data_'echo $1'.sql "
if [ ! -f $STRUCT_FILE ] ; then
    echo "File $STRUCT_FILE does not exists"
    exit 1
fi
if [ ! -f $DATA_FILE ] ; then
    echo "File $DATA_FILE does not exists"
    exit 2
fi
echo "structure: 'diff -d $STRUCT_FILE struct.sql | grep --regexp ^[\>\<] | wc -l' differences"
echo "data: 'diff -d $DATA_FILE data.sql | grep --regexp ^[\>\<] | wc -l' differences"
