# Tips

## Markdown

- https://www.markdownguide.org/basic-syntax/

## Git

### Init

0. `$ git init name.git`
1. `$ git remote -v; git remote add origin https://github.com/ThomasBucaioni/name.git; git remote -v`
2. `$ git pull`
3. `$ git push -u origin master`

### Branch

1. `git checkout master`; 
2. `git branch pr1`; 
2. `git checkout pr1`; 
2. edit files; 
2. `git add somefile1 somefile2`; 
2. `git commit`; 
2. `git push origin pr1`; 
2. `git checkout master`.

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

- `Ctrl-r`, `setopt no_flow_control`, `Ctrl-s`
- `C-e`, `C-a`, `C-r`
- `M-.`
- `M-#` (bash), `bindkey '^[#' pound-insert` (zsh)
- `C-d`, `C-w`
- `C-x`, `C-e`
- `C-u` (bash/zsh), `C-k`, `C-y`
- `cd !$`, `sudo !!`, `$1`, `$2`, `$3`, `$@`, `$0`, `$#`, `$*`, `$_`, `$?` ([see](https://devhints.io/bash) [special parameters](https://wiki.bash-hackers.org/syntax/shellvars#special_parameters_and_shell_variables))
- `ls | grep | sed 'p;s/a/b/' | xargs -n2 echo`, `mv`
- `sensors | awk '/Core/ {gsub("[+°C]","",$3), a=a+$3} END {print a/4}`
- `for i in $(seq 10); do echo $((a=a+i)) ; done`, `a=1 ; for i in $(seq 10); do echo $((a=a*i)) ; done`, `a=0; b=0; c=1; for i in $(seq 10); do echo "$((a=b)), $((b=c)), $((c=b+a))" ; done`
- `[[ 0 -eq $? ]] && echo true || echo false`
- `lsblk -f`, `mount -v -t /dev/sdX /mnt`, `lsblk`, `gdisk /dev/sdX (xzyy)`, `sudo dd if=new.iso of=/dev/sdX bs=1M status=progress`, `sudo umount -v /mnt`, `sudo fdisk -l`
- 

## Emacs

- `M-x M-p`
- `M-x tdoe`
- 

## NeoVim

- Copy-paste with `"+y` and `"+p` registers
- `vnoremap <C-C> y:call system("wl-copy --trim-newline", @")<cr>`, `inoremap <C-V> <ESC>:let @"=substitute(system("wl-paste --no-newline"), '<C-v><C-m>', '', 'g')<cr>pa`

## Screen command

- https://www.geeksforgeeks.org/screen-command-in-linux-with-examples/

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

- `echo -e  "<span foreground='#963000'> $xkb_switch ⌨️ </span>"\| "<span foreground='#c1a000'> </span><span foreground='#c16b26'>${Mem} <span foreground='#c1a000'>/ </span>${TotalMem}</span> <span foreground='#c1a000'>G</span>" \| "<span foreground='#c1a000'> </span><span foreground='#c16b26'>${load}</span>" \| "<span foreground='#c1a000'> </span><span foreground='#c16b26'>${fan}</span>" \| "<span foreground='#00ff00'> $ip </span>"\|   $date_formatted`
- `echo -e  ''   \| "<span foreground='#0088ff'> $weather</span>" \| "<span foreground='#c1a000'> <span foreground='#c16b26'>$disk_home</span> G</span> | <span foreground='#c1a000'> <span foreground='#c16b26'>$disk_root</span> G</span>" \| "<span foreground='#963000'> $check_updates 💎 $check_updates_aur 💻 $uptime_formatted ⬆️ $linux_version 🐧 </span>"\|"<span foreground='#ff0000'> $ram </span>"`

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
# Take a screenshot with all output and save it into screenshots (jpeg: -t jpeg)
bindsym Print exec grim ~/screenshots/$(date +%Y-%m-%d_%H-%M-%S).png
# Take a Screenshot with the region select (jpeg: -t jpeg) 
bindsym $mod+Print exec grim -g "$(slurp)" ~/screenshots/$(date +%Y-%m-%d_%H-%M-%S).png
```

## Dnsmasq

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

