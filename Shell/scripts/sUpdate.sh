#!/bin/bash
apt-get update &> /tmp/apt-list.log
apt-get upgrade -Ryq > /tmp/apt-info.log 2> /tmp/apt-error.log
if [ $? -eq 0 ] ; then
    aptitude clean
else
    cat /tmp/apt-error.log | mail -s "[Maintenance] Update failed" user@mail.com
fi
