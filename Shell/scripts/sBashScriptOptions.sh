#!/bin/bash

while [ True ]; do
if [ "$1" = "--alpha" -o "$1" = "-a" ]; then
    ALPHA=1
    shift 1
elif [ "$1" = "--config" -o "$1" = "-c" ]; then
    CONFIG=$2
    shift 2
else
    break
fi
done

echo $ALPHA
echo $CONFIG

ARG=( "${@}" )

for i in ${ARG[@]}; do
    echo $i
done

