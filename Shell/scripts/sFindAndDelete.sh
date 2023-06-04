#!/bin/bash
if [ ! $# -eq 1 ] ; then
    echo "Usage : ./script.sh db_name'"
    exit 1
fi
function deldatabase
{
    echo $FILE
    read -n 1 -p "Do you want to delete this file? [y/n] " CHOICE
    case $CHOICE in
	o|O )
	    echo "** $file deleted **"
	    rm $FILE
	    ;;
	n|N|* )
	    echo ".. file kept .."
	    ;;
    esac
}
for FILE in $(find . -name \*'echo $1'\*) ; do
    deldatabase $FILE
done
