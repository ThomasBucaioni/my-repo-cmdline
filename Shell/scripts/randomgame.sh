#!/bin/bash
seq 15 5 100 | shuf | head -2
seq 1 10 | shuf | head -4
echo $(( RANDOM % 800 + 200 ))
echo "Le compte est bon ?"
