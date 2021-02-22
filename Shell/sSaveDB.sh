#!/bin/bash
if [ ! $# -eq 1 ] ; then
    echo "Usage : './dump.sh db_name'"
    exit 1
fi
BASE=$1
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
mysqldump \
    --default-character-set=utf8 \
    --comments \
    --skip-extended-insert \
    --complete-insert \
    --no-create-db \
    --no-create-info \
    --skip-add-locks \
    --skip-disable-keys \
    --result-file=data.sql \
    --user=$USER \
    --password=$PASS \
    --databases \
    $BASE
if [ $? = "0" ] ; then
    echo "Import of data: success"
else
    echo "Import of data: FAIL"
    exit 3
fi
cp struct.sql struct_'date +%Y%m%d_%H%M%S'.sql
cp data.sql data_'date +%Y%m%d_%H%M%S'.sql
