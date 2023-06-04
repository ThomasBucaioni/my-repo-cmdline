#!/bin/bash
if [ ! $# -eq 1 ] ; then
    echo "Usage : ./script.sh timestamp'"
    exit 1
fi
if [ ! -d $1 ] || [ ! -d $2 ] ; then
    echo "The script takes directories as parameters"
    exit 2
fi
if [ $1 = $1 ] ; then
    SUFFIX="_mini"
else
    SUFFIX=""
fi
for source in $(find $1 -maxdepth 1 \( -name \*.jpg -o -name \*.png \) ) ; do
    FILE=$(basename "$source")
    destination="echo $2'/'echo ${FILE%.*}''echo $SUFFIX'.'echo ${FILE##*.}'"
    echo "conversion from $source to $destination"
    convert $source -resize 64x64\! $destination
done
