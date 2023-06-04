#!/bin/bash
#IFS= read -r text
#read -r moves
echo "$1" ::: "$2" | awk -F ':::' '{
    s = substr($1,1,length($1)-1)
    m = substr($2,2,1)
    printf "s=%s, m=%s\n", s, m
    for (i=1; i<length($2); i++){
    	print i, $2, $1
	if (m == "<") {s=substr(s,2,length(s)-1)substr(s,1,1)}
        if (m == ">") {s=substr(s,length(s),1)substr(s,1,length(s)-1)}
        print "s: ", s
    }
}'
echo "?"
