# Tips

## Markdown

- https://www.markdownguide.org/basic-syntax/

## Yaml

- https://yaml.org/refcard.html

## Git

### Init

0. `$ git init name.git`
1. `$ git remote -v; git remote add origin https://github.com/username/name.git; git remote -v`
2. `$ git pull`
3. `$ git push -u origin master`

### Ssh key identification

`$ git remote set-url origin git@github.com:user/my-repo.git`

### Branch

1. `git checkout master`
2. `git branch pr1`
2. `git checkout pr1`
2. edit files
2. `git add somefile1 somefile2`
2. `git commit`
2. `git push origin pr1`
2. `git checkout master`

### Sync fork

1. `git status`
2. `git remote -v`
2. `git remote add upstream https://github.com/org-repo`
2. `git remote -v`
2. `git fetch upstream`
2. `git checkout master`
2. `git merge upstream/master`

### Drop

1. `git rebase -i HEAD~4`
2. change 'pick' to 'drop'
2. `git push --force`

## Shell

- `Ctrl-r`, `setopt no_flow_control` (zsh), `stty -ixon` (bash), `Ctrl-s`
- `C-e`, `C-a`, `C-r`
- `M-.`
- `M-#` (bash), `bindkey '^[#' pound-insert` (zsh)
- `C-d`, `M-d`, `C-w`
- `C-x`, `C-e`
- `C-u` (bash/zsh), `C-k`, `C-y`
- `cd !$`, `sudo !!`, `$1`, `$2`, `$3`, `$@`, `$0`, `$#`, `$*`, `$_`, `$?` ([see](https://devhints.io/bash) [special parameters](https://wiki.bash-hackers.org/syntax/shellvars#special_parameters_and_shell_variables))
- `ls | grep | sed 'p;s/a/b/' | xargs -n2 echo`, `mv`
- `ls | awk '{printf("\"%s\"\n",$0); gsub("[ \047]","",$0); print $1}' | xargs -n2 echo`, `mv`
- `sensors | awk '/Core/ {gsub("[+°C]","",$3); a=a+$3; i++} END {print a/i}`
- `for i in $(seq 10); do echo $((a=a+i)) ; done`, `a=1 ; for i in $(seq 10); do echo $((a=a*i)) ; done`, `a=0; b=0; c=1; for i in $(seq 10); do echo "$((a=b)), $((b=c)), $((c=b+a))" ; done`
- `[[ 0 -eq $? ]] && echo true || echo false`
- `lsblk -f`, `mount -v -t /dev/sdX /mnt`, `lsblk`, `gdisk /dev/sdX (xzyy)`, `sudo dd if=new.iso of=/dev/sdX bs=1M status=progress`, `sudo umount -v /mnt`, `sudo fdisk -l`
- `find . -name "*.torrent" -exec rm -rf {} \;`
- `echo "keymaps 0-255\nkeycode  58 = Control\nkeycode  29 = Caps_Lock" > /etc/my_caps_ctrl.kmap`; `sudo loadkeys /etc/my_caps_ctrl.kmap`
- `gunzip dvorak.map.gz`, `sudo cp dvorak.map my_dvorak.map`, `vi my_dvorak.map`, `gzip my_dvorak.map`, `sudo cp ~/my_dovak.map.gz /usr/?lib?/kbd/keymaps/legacy/i386/dvorak/my_dvorak.map.gz`, `localectl set-keymap my_dvorak`
- `for file in $DIR/*my_string*.txt ; do echo "$file" ; done`, `for file in $DIR/*my_string*.txt ; do mv -nv -- "$file" "$file.$(date +%Y%m%d)" ; done`, `for file in *; do echo-mv "$" $(echo $file | sed 's/regex/replace_text/'); done`
- `du -h | sort -nr | head`
- `gnuplot -e 'plot for [file in system("find . -depth 1 -type f -print")] file u 3:2'`
- `until timeout 5s sleep 6 ; do echo $(( i=i+1 )) ; done`
- `^foo^bar^:G`, `!!:gs/foo/bar/`
- `line=$(sed -n '123p' file.txt | tr -s '\t' ' ' | cut -d' ' -f1)`
- `journalctl --vacuum-time=2d`, `journalctl --vacuum-size=100M`
- `for file in /proc/*/status ; do awk '/VmSwap|Name/{printf $2 " " $3}END{ print ""}' $file; done | sort -k 2 -n -r | less`
- `du --separate-dirs --all --time --threshold=1G --human-readable`
- `crontab -e`, `* * * * *	XDG_RUNTIME_DIR=/run/user/$(id -u) notify-send Hey "this is dog!"`
- `du -a . | sort -n -r | head -n 50`, `find -type f -exec du -Sh {} + | sort -rh | head -n 50`
- `convert image.heavy  new_image.light`, `ffmpeg -i audiofile_input.light -vn audiofile_output.light`, `ffmpeg -i input_video.heavy output_video.light`

### Misc (https://opensource.com/)

- `smem --pie name -c pss`
- `echo 'smem -c pss -P "$1" -k -t | tail -n 1' > ~/bin/memory-use && chmod +x ~/bin/memory-use`, `memory-use firefox`
- `sudo shred -vfz /dev/sdX`, `sudo dd if=shredos.img of=/dev/sdX bs=4M status=progress`, `sudo umount /dev/sdXY -l ; sudo dd if=/dev/urandom of=/dev/sdX bs=10M`, `sudo nvme sanitize /dev/nvme0nX`
- `wget --max-redirect 0 http://iana.org`, `--mirror`, `wget --continue https://example.com/linux-distro.iso`
- `ping -D 8.8.8.8`, `ping -s 2`, `ping -w 6`, `host example.com`
- procps-ng: `pidof bash`, `pgrep .sh`, `fuser --user ~/example.txt`, `ps 3234`, `ps -e | less`, `ps -U tux | less`, `pstree -U tux -u --show-pids`, `ps -U tux -u`, `pmap 1776`
- cron: `01 01 * * * /usr/local/bin/rsbu -vbd1 ; /usr/local/bin/rsbu -vbd2`, `03 05 * * * /sbin/hwclock --systohc`, `25 04 1 * * /usr/bin/dnf -y update`, `00 15 * * Thu /usr/local/bin/mycronjob.sh`, `02 03 1 1,4,7,10 * /usr/local/bin/reports.sh`, `01 09-17 * * * /usr/local/bin/hourlyreminder.sh`, `*/5 08-18/2 * * * /usr/local/bin/mycronjob.sh`, `04 07 * * * student /usr/local/bin/mycronjob.sh`, `/etc/cron.d`
- awk: `gawk 'pattern {action}' file1 file2 ...`, `gawk -F: '{print "uid", $3;}' /etc/passwd`, `gawk /^[A-Z]s/exp1/&exp2/g`
- irc: `/msg NickServ REGISTER password youremail@example.com`, `/msg NickServ IDENTIFY nick password`, `/query nick`, `/motd`, `/topic`
- net: `nslookup example.com`, `telnet example.com 110`, `openssl s_client -starttls smtp -connect example.com:587`, `netstat --listening --all --route  --interfaces`, `systemctl restart network`, `tcpdump -i eth0`,
- nmcli: `device`, `device show eth0`, `connection`, `connection up foo`, `device wifi connect foo`
- ip: `route`, `route add default gw 10.0.0.1`, `addr show`, `neighbor show`, `arp`
- firewall: `firewall-cmd --get-active-zones`, `-–change-interface eth0 --zone=example`, `--get-services`, `--add-service samba --zone=example`, `--add-port=123/tcp --zone=example`, `--permanent`
- ssh: `-D <port> <remote_host>`, `-L <port>:<target_host>:3389 <bastion_server>`, `-L 5901:localhost:5901 <remote_host>`, `ssh-keygen`, `ssh-keygen -p`, `ssh-copy-id -i <identity file> <remote_host>`, `-i <identity file>`, `-p <remote port>`, `-C`, `-D <port>`, `-X`, `-A `, `-4`, `-6`, `-L <local port>:<target host>:<target port>`
```
$ ssh myhouse
${HOME}/.ssh/config
host myhouse
 User itsme
 HostName house.example.com
```
- forward tunnel: `ssh -p vps-open-port -i ~/.ssh/vps-key vps-user@vps-public-ip -L localhost-random-port:vps-private-ip:vps-website-port-say-80`, `http://localhost:localhost-random-port`
- reverse tunnel: `ssh -v -p vps-open-port -i ~/.ssh/vps-key vps-user@vps-ip -R vps-random-port:localhost:localhost-open-port-say-22`, `ssh -v -p vps-random-port -i ~/.ssh/vps-key user-on-local-computer@vps-ip`

### Bash lists

| Syntax	| Result |
| :---        |    :----:   |
|arr=()	|Create an empty array|
|arr=(1 2 3)	|Initialize array|
|${arr[2]}	|Retrieve third element|
|${arr[@]}	|Retrieve all elements|
|${!arr[@]}	|Retrieve array indices|
|${#arr[@]}	|Calculate array size|
|arr[0]=3	|Overwrite 1st element|
|arr+=(4)	|Append value(s)|
|str=$(ls)	|Save ls output as a string|
|arr=( $(ls) )	|Save ls output as an array of files|
|${arr[@]:s:n}	|Retrieve n elements starting at index s|

### Prompt

- `export TERM=xterm-256color`
- `setxkbmap us -variant dvorak`

1. Bash

```
PS1="" # reset
PS1="$PS1\[\e[0m\]\[\e[03;32m\]\u" # user
PS1="$PS1\[\e[0m\]\[\e[01;35m\]@" # separator
PS1="$PS1\[\e[0m\]\[\e[01;36m\]\h" # host
PS1="$PS1\[\e[0m\]\[\e[01;35m\]:" # separator
PS1="$PS1\[\e[0m\]\[\e[48;5;95;38;5;214m\]\D{%d.%m@%H.%M.%S}" # date
PS1="$PS1\[\e[0m\]\[\e[01;35m\]:" # separator
PS1="$PS1\[\e[0m\]\[\e[01;34m\]\w" # path
PS1="$PS1\[\e[0m\]\[\e[01;35m\]:" # separator
PS1="$PS1\[\e[0m\]\[\e[01;37m\]$?" # last error code
PS1="$PS1\[\e[0m\]\[\e[01;35m\]:\$\[\e[00m\] " # ending
```

2. Zsh
```
PS1="%K{032}%B%n%b%k"
PS1="$PS1 %F{magenta}%K{grey}%B@%b%k%f"
PS1="$PS1 %K{green}%F{118}%B%m%b%f%k"
PS1="$PS1 %F{magenta}%K{grey}%B:%b%k%f"
PS1="$PS1 %K{054}%F{208} %T - %W %f%k"
PS1="$PS1 %F{blue}%F{magenta}%K{grey}%B:%b%k%f"
PS1="$PS1 %K{105}%F{11} %~/ %f%k%F{magenta}%K{grey}%B>%b%k %f"
RPS1="%(?.%F{green}0.%K{red}%F{011})%(?..(%?%))%(?.%f.%f%k)%F{magenta}%K{grey}:%k%f%F{105}%2c%f"
```

3. Bash root
```
RED='\[\033[0;31m\]'
WHITE='\[\033[1;37m\]'
GRAY='\[\033[0;37m\]'
BROWN='\[\033[0;33m\]'
PS1="$RED[$WHITE\u$BROWN@$WHITE\h$BROWN:$WHITE\W$RED] #$GRAY "
```

4. Bash admin
```
GREEN='\[\033[0;32m\]'
BROWN='\[\033[0;33m\]'
WHITE='\[\033[1;37m\]'
WHITEUNDLN='\[\033[4;37m\]'
GRAY='\[\033[0;37m\]'
CYAN='\[\033[0;36m\]'
PS1="$GREEN[$WHITE\u$CYAN@$WHITE\h$CYAN:$BROWN\w$GREEN] \$ $GRAY"

alias rm='rm -i'
alias mv='mv -i'
alias cp='cp -i'
alias ..='cd ..'
alias ...='cd ../..'
alias v='vim'
alias ve='sudo vim'
alias e='emacs'
alias se='sudo emacs'
```
### Screensaver

1. `xset s off`
2. `xset s noblank`
3. `xset dpms 0 0 0`
4. `xset -dpms`

## Emacs

- `M-x M-p`
- `M-x tdoe`
- `etags ~/dir/*.c`, `M-.`
- `M-x transparency`
- `C-u C-SPC`
- `(setq mouse-yank-at-point t)`

### Evil

- `~`, `g~` ; visual `u`, `U`, `guw`, `vim :help ~`

## NeoVim

- `"+y`, `"+p`
- `~/.config/nvim/init.vim`, `echom "I am here"`, `set termguicolors`, `set mouse=a`, `set nohlsearch`
- `vnoremap <C-C> y:call system("wl-copy --trim-newline", @")<cr>`, `inoremap <C-V> <ESC>:let @"=substitute(system("wl-paste --no-newline"), '<C-v><C-m>', '', 'g')<cr>pa`
- delete every other line: `:g/^/+d`

## Screen command

- https://www.geeksforgeeks.org/screen-command-in-linux-with-examples/
- `C-z :layout dump`
```
escape ^z^z

bindkey -k k6 prev
bindkey -k k7 next

bindkey -k k8 focus prev
bindkey -k k9 focus next

caption always " %w %= %c "
```

## Salt

### Checksum

- `sha1sum file`, `sha256sum file`, `md5sum file`
- `echo -n "my_string" | openssl dgst -sha256`, `echo -n "my_string" | sha256sum`

### Sha256 signature

- `openssl dgst -sha256 message.txt`
- `openssl dgst -sha256 -sign privatekey.pem -out signature.bin message.txt`
- `openssl dgst -sha256 -verify publickey.pem -signature signature.bin message.txt`

### ECDSA signature

- `openssl ecparam -genkey -name secp256k1 -noout -out eccprivatekey.pem`
- `openssl dgst -ecdsa-with-SHA1 -sign eccprivatekey.pem message.txt > ecsign.bin`
- `openssl dgst -ecdsa-with-SHA1 -verify eccpublickey.pem -signature ecsign.bin message.txt`
- `openssl req -new -key eccprivatekey.pem -x509 -nodes -days 365 -out ecccertificate.pem`
- `openssl x509 -in ecccertificate.pem -text -noout`

### Key generation, exchange, encryption

- `cat /etc/distrib-release`, `openssl version`
- `openssl genrsa -aes128 -out private_key.pem 1024`: 1024-bit public/private RSA key pair (+passphrase)
- `ls -l private_key.pem`, `file private_key.pem`, `head private_key.pem`
- `openssl rsa -in private_key.pem -noout -text`
- `openssl rsa -in private_key.pem -pubout > public_key.pem`
- `ls -l *.pem`
- `openssl rsa -in public_key.pem -pubin -text -noout`
- `echo "my text to encrypt" > secret.txt`
- `openssl rsautl -encrypt -inkey public_key.pem -pubin -in secret.txt -out secret.enc`, `hexdump -C ./secret.enc`
- `openssl rsautl -decrypt -inkey private_key.pem -in secret.enc > secret_decipher.txt`

### Clean fingerprints

- `mv ~/.ssh/known_hosts ~/.ssh/known_hosts.old`
- `ssh-keygen -R HOSTNAME`

### Certificates

from https://nps.edu/web/c3o/labtainers

#### Authority
- `openssl genrsa -des3 -out private/ca.key.pem 2048`
- `openssl rsa -in private/ca.key.pem -text`
- `openssl req -config openssl.cnf -new -x509 -days 1825 -extensions v3_ca -key private/ca.key.pem -out ca.crt.pem`

#### Server
- `openssl genrsa -des3 -out server.key.pem 1024`
- `openssl req -config openssl.cnf -new -key server.key.pem -out server.req.pem`
- `openssl ca -config openssl.cnf -in server.req.pem -out server.crt.pem -extensions server`

#### OCSP
- `openssl genrsa -des3 -out ocsp.key.pem 1024`
- `openssl req -config openssl.cnf -new -key ocsp.key.pem -out ocsp.req.pem`
- `openssl ca -config openssl.cnf -in ocsp.req.pem -out ocsp.crt.pem -extensions ocsp_ext`

## Arch

1. `loadkeys dvorak`
1. `ip link`
1. `ping archlinux.org`
   - `echo "[Match]\nName=enpXYZ\n\n[Network]\nDHCP=yes" > /etc/systemd/network/20-wired.network`
   - `systemctl start systemd-networkd.service`
   - `systemctl start dhcpcd.service`
   - `ping archlinux.org`
1. `timedatectl set-ntp true`
1. `fdisk -l`
1. `mkfs.ext4 /dev/sdXX`
1. `mkswap /dev/sdXY`
1. `mount /dev/sdXX /mnt`
1. `swapon /dev/sdXY`
1. `mount /dev/sdXZ /home`
1. `curl -s "https://archlinux.org/mirrorlist/?country=FR&country=GB&protocol=https&use_mirror_status=on" | sed -e 's/^#Server/Server/' -e '/^#/d' > /etc/pacman.d/mirrorlist.backup`
1. `pacman -Sy pacman-contrib`
1. `rankmirrors -n 10 /etc/pacman.d/mirrorlist.backup > /etc/pacman.d/mirrorlist`
1. `pacstrap /mnt base linux linux-firmware`
   - `vi /etc/pacman.d/gnupg/gpg.conf`, `keyserver hkp://keyserver.ubuntu.com`, `pacman-key --populate archlinux`, `pacman -Sc`
   - `pacman -Sy archlinux-keyring` 
   - `pacstrap /mnt base linux linux-firmware`
1. `genfstab -U /mnt >> /mnt/etc/fstab`, `vi /mnt/etc/fstab`
1. `arch-chroot /mnt`
1. `ln -sf /usr/share/zoneinfo/Region/City /etc/localtime`
1. `hwclock --systohc`
1. `echo "en_US.UTF-8 UTF-8" > /etc/locale.gen`
1. `locale-gen`
1. `echo LANG=en_US.UTF-8 > /etc/locale.conf`
1. `echo KEYMAP=dvorak > /etc/vconsole.conf`
1. `echo mypcname > /etc/hostname`
1. `echo "127.0.1.1	mypcname.localdomain	mypcname" > /etc/hosts`
1. `mkinitcpio -P`
1. `passwd`
1. `pacman -Sy grub os-prober`
1. `grub-install --target=i386-pc /dev/sdX`
1. `grub-mkconfig –o /boot/grub/grub.cfg`
1. `exit`
1. `reboot`

## Sway

### Bars

- `fan=$(sensors | awk '/^fan1/{print $2 " rpm"}')`
- `echo -e  "<span foreground='#c1a000'> </span><span foreground='#c16b26'> $fan </span>" \|`
- `tempcpu=$(sensors | awk '/Core/ {gsub("[+°C]","",$3); a=a+$3; i++} END {printf("%4.1f",a/i)}')`
- `tempgpu=$(sensors | awk '/^temp/ {gsub("[+°C]","",$2); print $2}')`
- `xkb_switch=$(swaymsg -t get_inputs | jq -r '.[] | select(.identifier == "1241:41096:HID_04d9:a088") | .xkb_active_layout_name')`
- `Mem=$(vmstat -s | sed -n 2p | sed s/[^0-9]//g)`, `Mem=$(echo "scale=1;${Mem}/1048576" | bc -l)`
- `TotalMem=$(vmstat -s | sed -n 1p | sed s/[^0-9]//g)`, `TotalMem=$(echo "scale=1;${TotalMem}/1048576" | bc -l)`
- `load=$(cut -d ' ' -f1 /proc/loadavg)`
- `disk_root=$(df -h -P -l '/' | awk '/G/ {print $4}' | sed 's/G//g')`, `disk_home=$(df -h -P -l ~ | awk '/G/ {print $4}' | sed 's/G//g')`
- `ip=$(hostname -i | awk '{ print "" $1 }')`
- `date_formatted=$(date "+%a %F %H:%M:%S")`

### Mako
```
exec mako
bindsym $mod+comma exec makoctl dismiss
bindsym $mod+period exec makoctl invoke
bindsym $mod+shift+comma  exec makoctl dismiss -a
bindsym $mod+shift+period exec makoctl menu wofi -d -p 'Choose Action: '
```

### Wheather
```
bindsym $mod+Scroll_Lock exec ~/bin/run_with_sway_command.sh 'floating enable, resize set 1200 800' \
kitty -e zsh -c 'curl https://wttr.in/ && read "?Press enter to continue"'
```

### Screenshots
```
# Take a screenshot with all outputs and save it into the $screenshots directory (jpeg format: -t jpeg)
bindsym Print exec grim ~/screenshots/$(date +%Y-%m-%d_%H-%M-%S).png
# Take a screenshot with the region selected (jpeg format: -t jpeg) 
bindsym $mod+Print exec grim -g "$(slurp)" ~/screenshots/$(date +%Y-%m-%d_%H-%M-%S).png
```

## Xubuntu

### StumpWM

- `(define-key *top-map* (stumpwm:kbd "s-F1") "exec slock")`
- `(define-key *top-map* (stumpwm:kbd "s-S-F2") "loadrc")`
- `(define-key *top-map* (stumpwm:kbd "s-F2") "gnew")`
- `(define-key *top-map* (stumpwm:kbd "s-F3") "exec kitty")`
- `(define-key *top-map* (stumpwm:kbd "M-F4") "delete")`
- `(define-key *top-map* (stumpwm:kbd "s-S-F12") "exec poweroff")`
- `(define-key *top-map* (stumpwm:kbd "s-Left") "move-focus left")`, `Down`, `Right`, `Up`
- `(define-key *top-map* (stumpwm:kbd "s-S-Left") "move-window left")`
- `(define-key *top-map* (stumpwm:kbd "s-n") "next-in-frame")`
- `(define-key *top-map* (stumpwm:kbd "s-o") "other-in-frame")`
- `(define-key *top-map* (stumpwm:kbd "s-;") "exchange-direction left")`
- `(define-key *top-map* (stumpwm:kbd "s-q") "exchange-direction right")`
- `(define-key *top-map* (stumpwm:kbd "s-'") "gnext")`
- `(define-key *top-map* (stumpwm:kbd "s-a") "gprev")`
- `(define-key *top-map* (stumpwm:kbd "s-\"") "gnext-with-window")`
- `(define-key *top-map* (stumpwm:kbd "s-A") "gprev-with-window")`

### Xfce

- `xfce4-panel`
- `xfce4-screenshoter`
- `blueman-manager`
- `xset s off`, `xset s noblank`, `xset dpms 0 0 0`, `xset -dpms`

## Networking

### Dnsmasq

1. `/etc/dnsmasq.conf`
```
server=8.8.8.8
server=8.8.4.4
interface=LAN-interface-on-GATEWAY
dhcp-range=172.168.1.2,172.168.1.5
```
2. `/etc/hosts`
```
127.0.0.1	localhost
127.0.1.1	gateway-hostname1or2
172.168.1.1	gateway-hostname2or1
172.168.1.2	mypc1-hostname
172.168.1.3	mypc2-hostname
```
3. `/etc/resolv.conf`
```
nameserver 127.0.0.1
```
4. `ip addr add 172.168.1.1/24 dev LAN-interface-on-GATEWAY`, ?`ip addr add 172.168.1.2/24 via 172.168.1.1 dev LAN-interface-on-HOST`, `ip route add default via 172.168.1.1 dev LAN-interface-on-HOST`
5. `iptables -t nat -A POSTROUTING -o WAN-interface-on-GATEWAY -j MASQUERADE`, `iptables -A FORWARD -i LAN-interface-on-GATEWAY -o WAN-interface-on-GATEWAY -j ACCEPT`
6. `sysctl net.ipv4.ip_forward`, `sudo sysctl -w net.ipv4.ip_forward=1`

### Isc-dhcp-server

1. `sudo apt install isc-dhcp-server`
2. `/etc/dhcp/dhcpd.conf`
```
default-lease-time 600;
max-lease-time 7200;
option subnet-mask 255.255.255.0;
option broadcast-address 172.168.1.255;
option routers 172.168.1.1;
option domain-name-servers 8.8.8.8, 4.4.4.4, 1.1.1.1;

subnet 172.168.1.0 netmask 255.255.255.0 {
option routers 172.168.1.1;
option subnet-mask 255.255.255.0;
option broadcast-address 172.168.1.255;
option domain-name-servers 8.8.8.8, 4.4.4.4, 1.1.1.1;
range 172.168.1.2 172.168.1.5;
default-lease-time 86400;
max-lease-time 86400;
} 
ddns-update-style none;
```
3. `/etc/default/isc-dhcp-server`
```
INTERFACESv4="LAN-interface-on-GATEWAY"
INTERFACESv6=""
```
4. iptables:
```
iptables -t nat -L POSTROUTING
iptables -L FORWARD
iptables -t nat -A POSTROUTING -o WAN-interface-on-GATEWAY -j MASQUERADE
iptables -A FORWARD -i LAN-interface-on-GATEWAY -o WAN-interface-on-GATEWAY -j ACCEPT
```

### Firewall

- `sudo ~/bin/firewall.sh`


## LVM & RAID ("[Administration Linux par la pratique T.1](https://www.eyrolles.com/Informatique/Livre/administration-linux-par-la-pratique-9782212677386/)", pp. 337-365)

### LVM

- `sudo fdisk -l /dev/sda`
- `sudo pvs`
- `sudo vgs`
- `sudo lvs`
- `lsblk`
- `sudo cfdisk /dev/sdk`, `8e`
- `sudo pvcreate /dev/sdb1`, `sudo pvs`
- `sudo vgextend vg0 /dev/sdb1`, `sudo pvs`, `sudo vgs`
- `sudo lextend -l +100%FREE /dev/mapper/vg0-root`, `sudo lvs`
- `sudo resize2fs /dev/mapper/vg0-root`, `df -h`

### RAID

- `cat /proc/mdstat`
- `sudo mdadm --detail /dev/md/root`, `boot`, `swap`
- `sudo mdadm --fail`
- `sudo mdadm --manage /dev/md125 --add /dev/sdb3`
- `sudo if=/dev/urandom of=/dev/sdb bs=512 count=5000000`, `sudo fdisk -l /dev/sdb`
- `# sfdisk -d /dev/sda | sfdisk /dev/sdb`
- `# mdadm --manage /dev/md125 --add /dev/sdb3`, `# watch cat /proc/mdstat`


## Grub

- `sudo grub2-mkconfig -o /boot/grub2/grub.cfg`
- `grep limit /etc/yum.conf`, `rpm -qa | grep kernel`,  `sudo package-cleanup --oldkernels --count=1`

## VPN

- `sudo cp file.opvn /etc/openvpn/client.conf`
- `remote vpnaddr1`, `remote vpnaddr2`, `remote-random`
- `auth-user-path /etc/openvpn/pass`, `login/npwd`
- `curl ifconfig.co`, `sudo openvpn --config /etc/openvpn/client.conf --daemon`, `curl ifconfig.co`
- `git clone https://aur.archlinux.org/openvpn-update-resolv-conf-git.git`

## Swap

- `sudo e /etc/sysctl.d/99-sysctl.conf`, `vm.swappiness=5`, `vm.vfs_cache_pressure=50`

## Logs

- `journalctl --disk-usage`
- `journalctl --vacuum-time=2d`, `journalctl --vacuum-size=100M`
- `se /etc/systemd/journald.conf`, `MaxFileSec=1month` , `SystemMaxUse=200M`
