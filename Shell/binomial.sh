#!/bin/bash
#read -r n

echo "$1" | awk '
    function factorial (n) {
        r = 1
        for (i = 2; i <= n; i++){
            r = r*i
            print "r=", r, "i=", i
            }
        return r
	}	
{
    N = factorial($1)
    for (j=0; j<=$1; j++){
        array[j] = N/factorial($1-j)/factorial(j)
        print "j=", j, "array[j]=", array[j]
    }
}
END {
    for (i in array) printf "%d ", array[i]
}
'
