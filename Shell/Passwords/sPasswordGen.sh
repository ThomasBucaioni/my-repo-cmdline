#!/bin/bash

#symbols array
symbolsArray=(A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 % $ \# @ ! \&)

#password string accumulator
passwordString="aA."

#length of the password
if [ -z $1 ]; then
    echo "Default password length is 16"
    #exit
    length=13
elif [[ $1 -ge 3 ]]; then
    echo "Password of length $1"
    length=$(($1 - 3))
else
    echo "Password of length 3"
    length=0
fi

#command for copy password to the clipboard
copy_to_clipboard_command="xclip -selection clipboard"
#uname=`uname`
windowman=`loginctl show-session $(awk '/tty/ {print $1}' <(loginctl)) -p Type | awk -F= '{print $2}'`

if [[ "$windowman" == "wayland" ]]; then
    copy_to_clipboard_command="wl-copy"
    echo 'Wayland copy to clipboard'
else
    echo 'Xclip copy to clipboard'
fi

#counter for loop
counter=0
while [ $counter -lt $length ]; do
    passwordString=$passwordString${symbolsArray[$(( ( RANDOM % ${#symbolsArray[*]} )  + 1 ))]}
    let counter=counter+1
done

echo $passwordString
echo $passwordString | $copy_to_clipboard_command
