#!/bin/bash

# Password directory
password_directory='/home/user/passwords/' # WARNING: absolute path needed

#command for copy password to the clipboard
copy_to_clipboard_command="xclip -selection clipboard"
windowman=`loginctl show-session $(awk '/tty/ {print $1}' <(loginctl)) -p Type | awk -F= '{print $2}'`

if [[ "$windowman" == "wayland" ]]; then
    copy_to_clipboard_command="wl-copy"
    echo 'Wayland copy to clipboard'
else
    echo 'Xclip copy to clipboard'
fi

#site
if [ -z $1 ]; then
    echo 'List of sites and logins'
    printf "\n"
    read -s -p "What is your master key? " masterkey
    printf "\n"

    echo ${password_directory}passwords_encrypted

    rm -rf passwords_decipher.txt
    openssl enc -aes-256-cbc -pbkdf2 -d -k $masterkey -in ${password_directory}passwords_encrypted -out ${password_directory}passwords_decipher.txt
    errorcode=$?

    #if the master key was correct
    if [[ $errorcode -eq 0 ]]; then
	awk -v "var=$mysite" 'BEGIN { FS = ":" } $0~var { printf "%s\t\t\t%s\n", $1, $2 }' ${password_directory}passwords_decipher.txt | uniq | sort
	rm -rf ${password_directory}passwords_decipher.txt
    else
	echo "Wrong password"
    fi
    exit
else
    mysite=$1
    echo "mysite = $mysite"
fi

printf "\n"
read -s -p "What is your master key? " masterkey
printf "\n"

echo ${password_directory}passwords_encrypted

rm -rf ${password_directory}passwords_decipher.txt
openssl enc -aes-256-cbc -pbkdf2 -d -k $masterkey -in ${password_directory}passwords_encrypted -out ${password_directory}passwords_decipher.txt
errorcode=$?

#if the master key was correct
if [[ $errorcode -eq 0 ]]; then
    line=$(awk -v "var=$mysite" 'BEGIN { FS = ":" } $0~var { print $1, $2, $3 }' ${password_directory}passwords_decipher.txt)
    awk -v "var=$mysite" 'BEGIN { FS = ":" } $0~var { print $1, $2, $3 }' ${password_directory}passwords_decipher.txt
    rm -rf ${password_directory}passwords_decipher.txt

    if [[ -z $2 ]]; then
	passwordString=$(echo $line | tr -s '\t' ' ' | cut -d' ' -f3)
    else
	passwordString=$(echo $line | tr -s '\t' ' ' | cut -d' ' -f $((3*$2)))
    fi
    #echo $line
    echo "Password : $passwordString"
    echo $passwordString | $copy_to_clipboard_command
else
    echo "Wrong password"
fi
