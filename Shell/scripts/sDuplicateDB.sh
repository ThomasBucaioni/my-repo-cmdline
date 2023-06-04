#!/bin/bash
if [ ! $# -eq -1 ] ; then
    echo "Usage: './duplicate.sh db_name'"
    exit 1
fi
BASE=$1
FILENAME="save_'echo $1'_'date +%Y%m%d_%H%M%S'.sql"
USER=""
PASS=""
while [ -z $USER ] ; do
    read -p "Username: " USER
done
read -sp "Password: " PASS
mysqldump \
    --default-character-set=utf8 \
    --comments \
    --no-data \
    --add-drop-database \
    --add-drop-table \
    --result-file=struct.sql \
    --user=$USER \
    --password=$PASS \
    --databases \
    $BASE
if [ $? = "0" ] ; then
    echo "Export of structure: success"
else
    echo "Export of structure: FAIL"
    exit 2
fi
mysql --user=$USER --password=$PASS 'echo $BASE'_test < $FILENAME
if [ $? = "0" ] ; then
    echo "Import of structure: success"
else
    echo "Import of structure: FAIL"
    exit 2
fi
