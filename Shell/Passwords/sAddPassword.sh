#!/bin/bash
#-----
# Adapted mainly from:
# https://github.com/KryDos/bash-password-generator/blob/master/password_generator.sh
# and also:
# https://linuxhandbook.com/read-command/#2-prompt-option-p
# https://linuxwebdevelopment.com/encrypt-files-openssl/
# https://devdojo.com/alexg/bash-random-password-generator
#-----

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


#symbols array
symbolsArray=(A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 % $ \# @ ! \&)

#password string accumulator
passwordString="aA0."

#site
if [ -z $1 ]; then
    echo 'Provide a context name'
    exit
else
    mysite=$1
    echo "mysite = $mysite"
fi
#login
if [ -z $2 ]; then
    echo 'Provide a login'
    exit
else
    mylogin=$2
    echo "mylogin = $mylogin"
fi
    #length of the password
if [ -z $3 ]; then
    echo 'Default password length is 20'
    #exit
    length=16
elif [[ $3 -ge 4 ]]; then
    echo "Password of length $1"
    length=$(($3 - 4))
else
    echo 'Password of length 4'
    length=0
fi

#counter for loop
counter=0
while [ $counter -lt $length ]; do
    passwordString=$passwordString${symbolsArray[$(( ( RANDOM % ${#symbolsArray[*]} )  + 1 ))]}
    let counter=counter+1
done

printf "\n"
read -s -p "What is your master key? " masterkey
printf "\n"

#decipher the passwords
rm -rf passwords_decipher.txt
openssl enc -aes-256-cbc -pbkdf2 -d -k $masterkey -in ${password_directory}passwords_encrypted -out ${password_directory}passwords_decipher.txt
errorcode=$?

#if the master key was correct
if [[ $errorcode -eq 0 ]]; then
    echo "$mysite:$mylogin:$passwordString" >> ${password_directory}passwords_decipher.txt
    openssl enc -aes-256-cbc -pbkdf2 -e -k $masterkey -in ${password_directory}passwords_decipher.txt -out ${password_directory}passwords_encrypted
    rm -rf ${password_directory}password_decipher.txt
    echo "Password added for site $mysite, login $mylogin: $passwordString"
    echo $passwordString | $copy_to_clipboard_command
else
    echo "Wrong password"
fi
