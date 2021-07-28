# L0

## Networking

- `sudo ip link set eth0 up`, `sudo dhclient eth0`
- `sudo ip link set eth0 up`, `sudo ip addr add 192.168.1.100 dev eth0`
- `ip link`, `ip -s link`, `ip -s link show eth0`
- `sudo ip link set eth0 down`
- `sudo ip link set eth0 mtu 1480`
- `sudo ip route add 172.16.1.0/24 via 192.168.1.5`
- `ip addr show eth0`, `ifconfig eth0`, `sudo ip link set eth0 down`, `sudo ip addr add 192.168.1.200 dev eth0`, `sudo ip link set eth0 up`, `sudo ifconfig eth0 down`, `sudo ifconfig eth0 up 192.168.1.100`, `sudo ip link set eth0 up`, `sudo dhclient eth0`, `sudo ifconfig eth0 up`, `sudo dhclient eth0`, `sudo reboot`

## Command details

### Basic commands and utilities

#### File compression

- `bunzip2`, `bzcat`, `bdiff`, `bzip2`, `bzless`, `gunzip`, `gzexe`, `gzip`, `zcat`, `zless`, `zip`, `upzip`, `xz`, `unxz`, `xzcat`

#### File ownership, permissions and attributes

- `attr`, `chgrp`, `chown`, `chmod`

#### File

- `awk`, `basename`, `cat`, `col`, `cp`, `cpio`, `csplit`, `cut`, `dd`, `diff`, `dirname`, `egrep`, `expand`, `file`, `fgrep`, `fmt`, `grep`, `head`, `join`, `less`, `more`, `sed`, `tail`, `ta`

#### Filesystem

- `cd`, `chroot`, `df`, `dirs`, `du`, `fdisk`, `fsck`, `fuser`, `ln`, `ls`, `mkdir`, `mv`, `pushd`, `popd`, `rm`, `rmdir`

#### Networking

- `arp`, `domainname`, `finger`, `ftp`, `host`, `hostname`, `ifconfig`, `netstat`

#### Job control

- `at`, `atrm`, `batch`, `crontab`, `exec`, `exit`, `ipcs`, `ipcrm`, `kill`, `killall`

#### Expression evaluation

- `bc`, `dc`, `eval`, `expr`, `factor`, `false`, `true`

### Monitoring

#### Processes and load monitoring utilities

- `top`, `uptime`, `ps`, `pstree`, `mpstat`, `iostat`, `sar`, `numastat`, `strace`
- packages: `procps`, `psmisc`, `pstree`, `sysstat`, `numactl`, `strace`

#### Memory monitoring utilities

- `free`, `vmstat`, `pmap`
- package: `procps`

#### I/O monitoring

- `iostat`, `iotop`, `sar`, `vmstat`
- packages: `sysstat`, `iotop`, `sysstat`, `procps`

#### Network monitoring utilities

- `netstat`, `iptraf`, `tcpdump`, `wireshark`
- packages: `netstat`, `iptraf`, `tcpdump`, `wireshark`

### Graphical monitoring tools

- `gnome-system-monitor`
- `ksysguard`

### Modules

- `insmod`, `rmod`, `lsmod`, `modprobe`, `modprode -r`
- `sudo /sbin/modprobe module_name.ko irq=12 debug=3`

### Device management

- `sudo mknod [-m mode] /dev/name type major minor`, `mknod -m 666 /dev/mycdrv c 254 1`
- `/etc/udev/udev.c`, `/etc/udev/rules.d`

### Managing system services

- `systemctl [options] command [name]`
- `systemctl`
- `systemctl list-units -t service --all`
- `systemctl list-units -t service`
- `sudo systemctl start foo`, `sudo systemctl start foo.service`, `sudo systemctl start /path/to/foo.service`
- `sudo systemctl stop foo.service`
- `sudo systemctl enable sshd.service`
- `sudo systemctl disable sshd.service`

### Stress

- `sudo [dnf|yum|zypper|apt-get] install stress stress-ng`
- `stress-ng --help`
- `stress -c 8 -i 4 -m 6 -t 20s`

## Users and groups

- `sudo /usr/sbin/useradd bjmoose`
- `sudo passwd bjmoose`
- `sudo /usr/sbin/userdel bjmoose`, `-r`

### Groups

- `sudo /usr/sbin/groupadd anewgroup`
- `sudo /usr/sbin/groupdel anewgroup`
- `groups bjmoose`
- `sudo /usr/sbin/usermod -aG anewgroup bjmoose`, `groups bjmoose`
- `sudo /usr/sbin/usermod -G rjsquirrel rjsquirrel`, `groups rjsquirrel`
- `id`

### Files, users and permissions

- `ls -lF file`

### Su and sudo

- `su -`
- `su root -c ls`, `su - root -c ls`
- `/etc/sudoers`
- `/usr/sbin/visudo`, `/usr/sbin/sudoedit /etc/sudoers`
- `man sudoers`
- `someuser ALL=(ALL) ALL`
- `chmod 440 /etc/sudoers.d/user`, `400`
- `sudo su`

## Linux filesystem

- Btrfs: https://btrfs.wiki.kernel.org/index.php/Main_Page, https://lwn.net/Articles/575841/

### Mounting filesystem

- `sudo mount [-t type] [-o options] device dir`
- `sudo mount /dev/sda8 /usr/local`
- `/etc/fstab`
- `sudo mount /dev/sda2   /boot`, `sudo mount LABEL=boot  /boot`, `sudo mount    -L boot  /boot`, `sudo mount UUID=26d58ee2-9d20-4dc7-b6ab-aa87c3cfb69a /boot`, `sudo mount   -U 26d58ee2-9d20-4dc7-b6ab-aa87c3cfb69a /boot`
- `sudo mount`
- `sudo mount 192.168.1.100:/ISO_IMAGES /mnt`
- `dd if=/dev/zero of=/tmp/part count=500 bs=1M`, `mkfs.ext4 /tmp/part`, `mkdir /tmp/mntpart`, `sudo mount -o loop /tmp/part /tmp/mntpart`, `df -T`, `sudo umount /tmp/mntpart`, `fsck.ext4 -f /tmp/part`, `dumpe2fs /tmp/part`, `tune2fs /tmp/part`

## Essential command line tools

- `find`, `locate`, `grep`, `sed`
- `ls`, `cat`, `rm`, `mv`, `mkdir`, `rmdir`, `file`, `ln`, `tail`, `head`, `less`, `more`, `touch`, `wc`

### Finding files

#### Command `find`

- `find [location] [criteria] [actions]`
- `find /etc -name "*.conf"`
- `find /etc -name "*.conf" -ls`
- `find /tmp /etc -name "*.conf" -or -newer /tmp/.X0-lock -ls`
- `find . -name "*~" -exec rm {} ';'` ++
- `find . -name "*~" | xargs rm`
- `for names in $(find . -name "*~" ) ; do rm $names ; done`
- `find . -name "*~" -print0 | xargs -0 rm` +

#### Command `locate`

- `locate .conf`
- `locate --help`
- `sudo updatedb`

#### Command `grep`

- `grep pig file`
- `grep -i -e pig -e dog -r .`
- `grep "^dog" file`
- `grep "dog$" file`
- `grep d[a-p] file`
- `-i`, `-v`, `-n`, `-H`, `-a`, `-I`, `-r`, `-l`, `-L`, `-c`, `-e`

#### Command `sed`

- `sed s/pig/cow/ file > newfile`
- `sed s/pig/cow/ < file > newfile`
- `cat file | sed s/pig/cow/ > newfile`
- `sed s/pig/cow/g file > newfile`
- `sed s:pig:cow:g file > newfile`
- `sed s/'\\'/'\/'/g file > newfile`
- `echo "$HOME"`
- `echo '$HOME'`
- `sed -e s/"pig"/"cow"/g -e s/"dog"/"cat"/g < file > newfile`
- `echo hello | sed s/"hello"/"goodbye"/g`
- `cat scriptfile`
- `sed -f scriptfile < file > newfile`

#### Examples

- `find /tmp -newer /tmp/tstfile -ls`, `find /etc -name "*.conf"`, `find /etc -type d`, `find / -name "*.bak" -exec rm {}';'`
- `grep ftp /etc/services`, `grep ftp /etc/services | grep tcp`, `grep -n ftp /etc/services | grep -v tcp`, `grep 'ˆts' /etc/services`, `grep 'st$' /etc/services`

## Bash scripting

### Script basics

- `$0`, `$1`, `$2`, `$*`, `$@`, `$#`
- `shift n`
- `. file`, `source file`
- `set -n` (`bash -n`), `set -x` (`bash -x`), `set -v` (`bash -v`), `set -u` (`bash -u`), `set -e` (`bash -e`)
- `set +n` (`bash +n`), `set +x` (`bash +x`), `set +v` (`bash +v`), `set +u` (`bash +u`), `set +e` (`bash +e`)

### Conditionals

- `if [[ -f file.c ]] ; then ; fi`
- `if [ -f file.c ] ; then ; fi` (deprecated: `if [ $VAR == "" ]`, `​if [ "$VAR" == "" ]`)
- `if test -f file.c ; then ; fi` (deprecated: same)
- `$?`
- `make && make modules_install && make install`
- `[[ -f /etc/foo.conf ]] || echo 'default config' >/etc/foo.conf`
- `[[ $STRING == mystring ]] && echo mystring is "$STRING"`

### File conditionals

- `man 1 test`
- `-e file`, `-d file`, `-f file`, `-s file`, `-g file`, `-u file`, `-r file`, `-w file`, `-x file`

### String and arithmetic comparisons

- `string`, `string1 == string2`, `string1 != string2`, `-n string`, `-z string`
- `exp1 -op exp2`, `-eq, -ne, -gt, -ge, -lt, -le`
- `!`

### Case

- `#!/bin/sh`, `echo "Do you want to destroy your entire file system?`, `read response`, `case "$response" in`, `"yes") echo "I hope you know what you are doing!" ;;`, `"no" ) echo "You have some comon sense!" ;;`, `"y" | "Y" | "YES" ) echo "I hope you know what you are doing!" ;`, `echo 'I am going to type: " rm -rf /"';;`, `"n" | "N" | "NO" ) echo "You have some comon sense!" ;;`, `* ) echo "You have to give an answer!" ;;`, `esac`, `exit 0`

### Loops

#### For

- `for file in $(find . -name "*.o")`, `do`, `echo "I am removing file: $file"`, `rm -f "$file"`, `done`
- `find . -name "*.o" -exec rm {} ';'`
- `find . -name "*.o" | xargs rm`

#### While

- `​#!/bin/sh`, `ntry_max=4 ; ntry=0 ; password=' '`, `while [[ $ntry -lt $ntry_max ]] ; do`, `ntry=$(( $ntry + 1 ))`, `echo -n 'Give password:  '`, `read password`, `if  [[ $password == "linux" ]] ; then`, `echo "Congratulations: You gave the right password on try $ntry!"`, `exit 0`, `fi`, `echo "You failed on try $ntry; try again!"`, `done`, `echo "you failed $ntry_max times; giving up"`, `exit -1`

#### Until

- `#!/bin/sh`, `ntry_max=4 ; ntry=0 ; password=' '`, `until [[ $ntry -ge $ntry_max ]] ; do`, `ntry=$(( $ntry + 1 ))`, `echo -n 'Give password:  '`, `read password`, `if [[ $password == "linux" ]] ; then`, `echo "Congratulations: You gave the right password on try $ntry!"`, `exit 0`, `fi`, `echo "You failed on try $ntry; try again!"`, `done`, `echo "you failed $ntry_max times; giving up"`, `exit -1`

### Functions

- `#!/bin/sh`, `test_fun1(){`, `var=FUN_VAR`, `shift`, `echo " PARS after fun shift: $0 $1 $2 $3 $4 $5"`, `}`, `var=MAIN_VAR`, `echo ' '`, `echo "BEFORE FUN MAIN, VAR=$var"`, `echo " PARS starting in main: $0 $1 $2 $3 $4 $5"`, `test_fun1 "$@"`, `echo " PARS after fun in main: $0 $1 $2 $3 $4 $5"`, `echo "AFTER FUN MAIN, VAR=$var"`, `exit 0`
- `function fun_foobar(){`, `statements`, `}`, `function fun_foobar{`, `statements`, `}` (not in sh)

### Examples

#### Simple bash script

- `#!/bin/sh`, `nproc=$(ps | wc -l)`, `echo "You are running $nproc processes"`, `exit 0`

#### Simple backup script

- `#!/bin/sh`, `usage="Usage: Backup Source Target"`, `if [[ $# -lt 2 ]] ; then`, `echo -e '\n'    $usage '\n'`, `exit 1 `, `fi`, `if ! [[ -d $1 ]] ; then`, `echo -e '\n' ERROR: First argument must be a Directory that exists: quitting'\n'`, `exit 1`, `fi`, `SOURCE=$1`, `TARGET=$2`, `DIRLIST=$(cd $SOURCE ; find . -type d )`, `for NAMES in $DIRLIST`, `do`, `SOURCE_DIR=$SOURCE/$NAMES`, `TARGET_DIR=$TARGET/$NAMES`, `echo "SOURCE= $SOURCE_DIR      TARGET=$TARGET_DIR"`, `FILELIST=$( (cd $SOURCE_DIR ; find . -maxdepth 1 ! -type d ) )`, `mkdir -p $TARGET_DIR`, `OLDIFS=$IFS`, `IFS=''`, `tar -zcvf $TARGET_DIR/Backup.tar.gz  -C $SOURCE_DIR $FILELIST`, `IFS=$OLDIFS`, `done`

## Files and filesystem

- `ls -lF`, `-`, `d`, `l`, `p`, `s`, `b`, `c`
- `file *`
- `ls -l a_file`
- `chmod uo+x,g-w a_file`, `chmod 755 a_file`
- `chgrp aproject a_file`
- `chown coop a_file`, `chown coop.aproject a_file`, `chown -R coop.aproject .`, `chown -R coop.aproject subdir`
- `umask`, `umask 0022`, `umask -S`, `umask u=r,g=w,o=rw`


<!------ DevOps ------>

# DevOps

## Docker

### Port cleaning

- `sudo lsof -i tcp:8080`, `sudo kill -9 PID` 

<!------ L1 ------>

# L1

## Disk space

- `ls -F`
- `sudo du -shxc --exclude=proc *`
- `file /usr/lib/zsh/5.8/zsh/*`
- `sudo du --max-depth=1 -hx /`
- https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf

## Signals

- `SIGKILL=9`, `SIGSTOP=19`, `SIGTERM=15`
- `kill -l`
- `man 7 signal`
- `killall`, `pkill`

## Package management

- `# rpmbuild --rebuild -rb p7zip-16.02-16.el8.src.rpm`
- `# root/rpmbuild>find . -name "*rpm"`
- https://mirrors.edge.kernel.org/pub/software/scm/git/docs/
- `which git`, `git diff`, `git log`

### RPM

- https://rpm.org/
- `ls /usr/lib/rpm | wc -l`, `cat /usr/lib/rpm/rpmrc`
- `rpm -q -f -i -a -l -p --requires --whatprovides`
- `rpm -VaS5DMLUGT`
- `sudo rpm -ivh bash-4.4.19-12.el8_0.x86_64`
- `sudo rpm -e system-config-lvm`
- `sudo rpm --test -e xz`
- `rpm -qil bzip2 | less`, `ls -lF $(rpm -ql bzip2)`
- `rpm -Uvh bash-4.4.19-12.el8.x86_64.rpm`
- `sudo rpm -Fvh *.rpm`
- `sudo rpm -ivh kernel-{version}.{arch}.rpm`
- `rpm2archive bash-XXXX.rpm`
- `rpm -qilp package.rpm`
- `cd /var/lib`, `sudo cp -a rpm rpm_BACKUP`, `sudo rpm --rebuilddb`, `ls -l rpm rpm_BACKUP`, `rpm -qa | tee /tmp/rpm-qa.output`, `ls -l rpm rpm_BACKUP`, `sudo rm -rf rpm_BACKUP`

### DPKG

- `dpkg -S logrotate.conf`
- `dpkg -L logrotate`
- `dpkg -V logrotate`
- `sudo dpkg -r logrotate`

### Dnf

- `sudo dnf update`, `check-update`, `list updates`
- `list installed "*kernel*"`, `list installed "*kernel*"`
- `sudo dnf search bash`, `dnf list bash`, `dnf info bash`, `dnf deplist bash`
- `dnf grouplist`, `dnf groupinfo "Virtualization Host"`, `sudo dnf groupinstall "Virtualization Host"`, `sudo dnf groupremove "Virtualization Host"`
- `touch /etc/yum.repos.d/webmin.repo`,
```
[Webmin]
name=Webmin Distribution Neutral
baseurl=http://download.webmin.com/download/yum
mirrorlist=http://download.webmin.com/download/yum/mirrorlist
enabled=1
gpgcheck=0
```
- `sudo dnf install webmin`

### Zypper

- `zypper list-updates`
- `zypper repos`
- `zypper search <string>`
- `zypper info package`
- `zypper search --provides /usr/bin/exec`
- `sudo zypper install package`, `sudo zypper --non-interactive install package`
- `sudo zypper update`, `sudo zypper --non-interactive update`
- `sudo zypper remove package`
- `sudo zypper shell`
- `sudo zypper addrepo URL url-alias`
- `sudo zypper removerepo alias`
- `sudo zypper clean [--all]`
- `zypper search -d bash`
- `zypper info --requires  bash`
- `sudo zypper remove --dry-run bash`

### Apt

#### Resources

- https://www.debian.org/distrib/packages
- https://packages.ubuntu.com/

#### Basic commands

- `sudo apt-get install apt-file`, `sudo apt-file update`
- `apt-cache search "package-name"`
- `apt-cache show package-name`
- `apt-cache showpkg package-name`
- `apt-cache depends package-name`
- `apt-cache pkgnames`, `apt-cache pkgnames "package-name"`
- `dpkg --get-selections "*string*"`
- `apt-file search package-file-name`
- `apt-file list package-name`
- `sudo apt-get remove package-name`
- `sudo apt-get --purge remove package-name`
- `sudo apt-get update`
- `sudo apt-get upgrade`
- `sudo apt-get dist-upgrade`
- `sudo apt-get autoremove`
- `sudo apt-get clean`
- `apt-cache depends bash`, `apt-cache rdepends bash`
- `apt-cache search metapackage`

## System monitoring

### Processes

- `top`
- `uptime`
- `ps`
- `pstree`
- `mpstat`
- `iostat`
- `sar`
- `numastat`
- `strace`

### Memory

- `free`
- `vmstat`
- `pmap`

### I/O

- `iostat`
- `sar`
- `vmstat`

### Network

- `netstat`
- `iptraf`
- `tcpdump`
- `wireshark`

### Examples

- `sudo sar 3 3`, `-A`, `-b`, `-B`, ...
- `sudo tail -f /var/log/messages`, `syslog`, `boot.log`, `dmesg` , `secure`
- `cat /etc/logrotate.conf`
- `top`, `1`
- `vmstat -a 2 1000`
- `git clone git://kernel.ubuntu.com/cking/stress-ng.git`, `cd stress-ng`, `make`, `sudo make install`
- `stress-ng --help`, `info stress-ng`
- `stress-ng -c 8 -i 4 -m 6 -t 20s`, `stress-ng -m 4 -t 20s`

## Process Monitoring

- `ps aux`
- `ps -elf` ++
- `ps -eL`
- `ps -C "bash"`
- `ps -o pid,user,priority,cputime,pmem,size,command`
- `pstree -aAp process-id`
- `ls -l /proc/process-id/task`
- `top`, `k`, `h`
- `nice -n 10 bash`, `renice 15 -p process-id`
- `dd if=/dev/urandom of=/dev/null &`, `ps -C dd -o pid,cmd,stat`
- `fg`, `jobs`

## Memory monitoring

- `cat /proc/meminfo`
- `ls /proc/sys/vm`
- `vmstat 2 4`, `vmstat -a 2 4`, `vmstat -SM -a 2 4`
- `cat /proc/sys/vm/overcommit_memory`, `/proc/sys/vm/overcommit_ratio`
- `cat /proc/[pid]/oom_score`

## I/O Monitoring

- `iostat`, `iotop`, `ionice`
- `iotop -o`, `-m`, `-k`, `-N`
- `ionice -c 2 -n 3 -p [pid]`
- `time sudo bonnie++ -n 0 -u 0 -r 100 -f -b -d /mnt`, `bon_csv2txt < bonnie++.out > bonnie++.txt`

## FS and VFS

- `ln`, `ls -liF`
- `cat /proc/filesystems`
- `dd if=/dev/zero of=junk bs=1M count=512`, `sudo /sbin/mkfs.xfs junk`, `sudo mount junk /mnt`, `df -h`, `lsmod`
- `sudo mkdir /mnt/tmpfs`, `sudo mount -t tmpfs none /mnt/tmpfs`, `df -h /mnt/tmpfs`, `sudo mount -t tmpfs -o size=1G none /mnt/tmpfs`, `sudo umount /mnt/tmpfs`
- `df -h /dev/shm`, `df -h | grep 'tmpfs'`

## Disk partitioning

- `sudo fdisk -l /dev/sda | grep -i sector`
- `ls -l`, `sudo mkfs.ext4 /dev/sdxy`
- `sudo blkid /dev/sdx*`
- `lsblk`
- `dd if=/dev/sda of=mbrbackup bs=512 count=1`, `sudo dd if=mbrbackup of=/dev/sdx bs=512 count=1`, `sudo sgdisk -p /dev/sda`
- `fdisk`, `sfdisk`, `parted`, `gparted`, `gdisk`, `sgdisk`
- `sudo partprobe -s`, `cat /proc/partitions`
- `mkfs.ext4 /dev/sdxy`
- `dd if=/dev/zero of=imagefile bs=1M count=1024`, `mkfs.ext4 imagefile`, `mkdir mntpoint`, `sudo mount -o loop imagefile mntpoint`, `sudo umount mntpoint`
- `sudo losetup /dev/loop2 imagefile`, `sudo mount /dev/loop2 mntpoint`, `sudo umount mntpoint`, `sudo losetup -d /dev/loop2`
- `sudo fdisk -C 130 imagefile`, `n`, `+256M`
- `sudo losetup -f`, `sudo losetup /dev/loop1 imagefile`, `losetup -a`, `sudo parted -s /dev/loop1 mklabel msdos`, `sudo parted -s /dev/loop1 unit MB mkpart primary ext4 0 256`, `sudo parted -s /dev/loop1 unit MB mkpart primary ext4 256 512`, `sudo parted -s /dev/loop1 unit MB mkpart primary ext4 512 1024`, `fdisk -l /dev/loop1`, `ls -l /dev/loop1*`, `sudo mkfs.ext3 /dev/loop1p1`, `sudo mkfs.ext4 /dev/loop1p2`,`sudo mkfs.ext4 /dev/loop1p3`, `mkdir mnt1 mnt2 mnt3`, `sudo mount /dev/loop1p1 mnt1`, `sudo mount /dev/loop1p2 mnt2`, `sudo mount /dev/loop1p3 mnt3`, `df -Th`, `sudo umount mnt1 mnt2 mnt3`, `rmdir mnt1 mnt2 mnt3`, `sudo losetup -d /dev/loop1`

## Filesystem features: attributes, creating, checking, mounting

- `lsattr`, `chattr`
- `sudo mkfs -t ext4 /dev/sdxy`, `sudo mkfs.ext4 /dev/sd`
- `mount -t ext /dev/sdxy /home`
- `sudo mount LABEL=`, `-L`, `UUID`, `-U`
- `sudo mount -o remount,ro /myfs`
- `umount /dev/sdx`, `fuser`, `lsof`
- `sudo mount -t nfs myserver.com:/shdir /mnt/shdir​`
- `/etc/fstab`, `LABEL=Sam128 /SAM ext4 noauto,x-systemd.automount,x-systemd.device-timeout=10,x-systemd.idle-timeout=30 0 0`, `sudo systemctl daemon-reload`, `sudo systemctl restart local-fs.target`
- `df -h -T`
- `sudo mount -o ro,loop,noexec ~/imagefile ~/mntpoint`
- `/etc/fstab`, `/home/user/imagefile /home/user/mntpoint ext4 loop(defaults) 1 2`, `sudo mount -o remount ~/mntpoint`
- `/etc/fstab`, `/home/user/imagefile /home/user/mntpoint ext4 loop(-),ro,noexec 1 2`, `sudo mount -o remount ~/mntpoint`

## Filesystem features: swap, quotas, usage

- `df`, `-h`, `-T`, `-i`
- `du`, `-a`, `-h`, `-h somedir`
- `find . -maxdepth 1 -type d -exec du -shx {} \; | sort -hr`
- `cat /proc/swaps`, `free -m`
- `sudo mount -o remount /home`, `sudo quotacheck -vu /home`, `sudo quotaon -vu /home`, `sudo edquota someusername`
- `sudo quotaon -av`, `sudo quotaoff -av`, `-avu`, `-avg`
- `sudo quota user`
- `sudo edquota -u user`, `sudo edquota -g group`, `sudo edquota -u -p userproto user`, `sudo edquota -t`
- `cat /proc/swaps`, `dd if=/dev/zero of=swpfile bs=1M count=1024`, `mkswap swpfile`, `sudo swapon swpfile`, `sudo chown root:root swpfile`, `sudo chmod 600 swpfile`, `cat /proc/swaps`, `sudo swapoff swpfile`, `sudo rm swpfile`
- `e /etc/fstab`, `/imagefile /mnt/tempdir ext4 loop,usrquota 1 2`, `sudo mount -o remount /mnt/tempdir`, `sudo quotacheck -u /mnt/tempdir`, `sudo quotaon -u /mnt/tempdir`, `sudo chown student.student /mnt/tempdir`, `sudo edquota -u student`, `cd /mnt/tempdir`, `dd if=/dev/zero of=bigfile1 bs=1024 count=200`, `quota`, `dd if=/dev/zero of=bigfile2 bs=1024 count=400`, `quota`, `dd if=/dev/zero of=bigfile2 bs=1024 count=600`

## The ext4 Filesystem

- `sudo dumpe2fs /dev/sdb1`
- `sudo tune2fs -c 25 /dev/sda1`
- `sudo tune2fs -i 10 /dev/sda1`, `tune2fs -i 3w imagefile`
- `sudo tune2fs -m 10 /dev/sda1`
- `sudo tune2fs -l /dev/sda1`
- `sudo e4defrag -c /var/log`
- `dumpe2fs imagefile > dumpe2fs-output`, `grep -i  -e "Mount count" -e "Check interval" -e "Block Count" dumpe2fs-output`, `diff dumpe2fs-output-initial dumpe2fs-output-final`

## The Xfs and Btrfs filesystems

- `man -k xfs`
- `btrfs`, `btrfs --help`, `man -k btrfs`

## Encrypting disks

- `cryptsetup --help`
- `sudo cryptsetup luksFormat /dev/sdc12`, `sudo cryptsetup luksFormat --cipher aes /dev/sdc12`
- `sudo cryptsetup --verbose luksOpen /dev/sdc12 SECRET`
- `sudo mkfs.ext4 /dev/mapper/SECRET`
- `sudo mount /dev/mapper/SECRET /mnt`
- `sudo umount /mnt`
- `sudo cryptsetup --verbose luksClose SECRET`
- `/etc/fstab`, `/dev/mapper/SECRET /mnt ext4 defaults 0 0`
- `/etc/crypttab`, `SECRET ​/dev/sdc12`
- `man crypttab`
- `losetup -f`, `sudo losetup /dev/loop0 imagefile`, `losetup -l`, `sudo cryptsetup luksFormat /dev/loop0`, `sudo cryptsetup luksOpen /dev/loop0 cryptimage`, `ls -l /dev/mapper/`, `sudo mkfs.ext4 /dev/mapper/cryptimage`, `sudo mount /dev/mapper/cryptimage /mnt/`, `df -h`, `sudo umount /mnt`, `sudo cryptsetup luksClose /dev/mapper/cryptimage`, `sudo losetup -d /dev/loop0`, `losetup -l` (`rm imagefile`)
- `sudo fdisk /dev/sda`, `sudo partprobe -s`, `sudo cryptsetup luksFormat /dev/sda4`, `sudo cryptsetup luksOpen /dev/sda4 secret-disk`, `/etc/crypttab`, `sudo mkfs -t ext4 /dev/mapper/secret-disk`, `sudo mkdir -p /secret`, `/etc/fstab`, `/dev/mapper/secret-disk    /secret    ext4    defaults 1 2`, `sudo mount /secret` , `sudo mount -a`, `reboot`
- `cat /proc/swaps`, `sudo swapoff /dev/sda11`, `sudo cryptsetup luksFormat /dev/sda11  # --cipher aes`, `sudo cryptsetup luksOpen   /dev/sda11  swapcrypt`, `sudo mkswap /dev/mapper/swapcrypt`, `sudo swapon /dev/mapper/swapcrypt`, `cat /proc/swaps`, `sudo swapoff /dev/mapper/swapcrypt`, `sudo cryptsetup luksClose swapcrypt`, `sudo mkswap /dev/sda11`, `sudo swapon -a`, `/etc/fstab`, `/dev/sda11  swap   swap  defaults 0 0`, `sudo mkswap -L SWAP /dev/sda11`, `LABEL=SWAP  swap   swap  defaults 0 0`

## Logical Volume Managment

- `vgcreate`, `vgextend`, `vgreduce`
- `pvcreate`, `pvdisplay`, `pvmove`, `pvremove`
- `man lvm`
- `ls -lF /sbin/lv*`, `ls -lF /sbin/pv*`, `ls -lF /sbin/vg*`
- `lvcreate`, `lvdisplay`
- `fdisk`, `8e`
- `sudo pvcreate /dev/sdb1`
- `sudo pvcreate /dev/sdc1`
- `sudo vgcreate -s 16M vg /dev/sdb1`
- `sudo vgextend vg /dev/sdc1`
- `sudo lvcreate -L 50G -n mylvm vg`
- `sudo mkfs -t ext4 /dev/vg/mylvm`
- `sudo mkdir /mylvm`
- `sudo mount /dev/vg/mylvm /mylvm`
- `/etc/fstab`, `/dev/vg/mylvm /mylvm ext4 defaults 1 2`
- `pvdisplay`, `pvdisplay /dev/sda5`
- `vgdisplay`, `vgdisplay /dev/vg0`
- `lvdisplay`, `lvdisplay /dev/vg0/lvm1`
- `sudo lvresize -r -L 20 GB /dev/VG/mylvm`
- `sudo lvresize -r -L +100M /dev/vg/mylvm`
- `sudo pvmove /dev/sdc1`
- `sudo vgreduce vg /dev/sdc1`
- `sudo lvcreate -l 128 -s -n mysnap /dev/vg/mylvm`
- `mkdir /mysnap`
- `mount -o ro /dev/vg/mysnap /mysnap`
- `sudo umount /mysnap`
- `sudo lvremove /dev/vg/mysnap`
- `sudo fdisk /dev/sda`, `sudo partprobe -s`, `sudo pvcreate /dev/sdaX`, `sudo pvcreate /dev/sdaY`, `sudo pvdisplay`, `sudo vgcreate myvg /dev/sdaX /dev/sdaY`, `sudo vgdisplay`, `sudo lvcreate -L 300M -n mylvm myvg`, `sudo lvdisplay`, `sudo mkfs.ext4 /dev/myvg/mylvm`, `sudo mkdir /mylvm`, `sudo mount /dev/myvg/mylvm /mylvm`, `/etc/fstab`, `/dev/myvg/mylvm /mylvm ext4 defaults 0 0`, `sudo lvdisplay`, `df -h`, `sudo lvresize -r -L 350M /dev/myvg/mylvm`, `df -h`, or `sudo lvresize -r -L +50M /dev/myvg/mylvm`, or `df -h`, `sudo lvextend -L 350M /dev/myvg/mylvm`, `sudo resize2fs /dev/myvg/mylvm`, `df -h`

## Raid

- `mdadm`
- `/dev/mdX`
- `fdisk`, `fd`, `mdadm`, `/etc/fstab`
- `sudo fdisk /dev/sdb`, `sudo fdisk /dev/sdc`
- `sudo mdadm --create /dev/md0 --level=1 --raid-disks=2 /dev/sdbX /dev/sdcX`
- `sudo mkfs.ext4 /dev/md0`
- `sudo bash -c "mdadm --detail --scan >> /etc/mdadm.conf"`
- `sudo mkdir /myraid`
- `sudo mount /dev/md0 /myraid`
- `/etc/fstab`, `/dev/md0 /myraid ext4 defaults 0 2`
- `cat /proc/mdstat`
- `sudo mdadm -S /dev/md0`, `cat /proc/mdstat`, `sudo systemctl start mdmonitor`, `sudo systemctl enable mdmonitor`
- `sudo mdadm --create /dev/md0 -l 5 -n3 -x 1 /dev/sda8 /dev/sda9 /dev/sda10 /dev/sdb2`
- `sudo mdadm --fail /dev/md0 /dev/sdb2`
- `sudo mdadm --remove /dev/md0 /dev/sdb2`
- `sudo mdadm --add /dev/md0 /dev/sde2`

## Kernel Services and Configuration

- `cat /proc/cmdline`
- `man bootparam`
- `sysctl -a`
- `sudo sh -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'`, `sudo sysctl net.ipv4.ip_forward=1`
- `/etc/sysctl.conf`, `man sysctl.conf`, `sudo sysctl -p` (`/usr/lib/sysctl.d/`, `/etc/sysctl.d`)
- `sudo sysctl net.ipv4.icmp_echo_ignore_all=1`, `ping localhost`, `se /etc/sysctl.conf`, `net.ipv4.icmp_echo_ignore_all=1`, `sysctl -p`, `sysctl net.ipv4.icmp_echo_ignore_all`, `ping localhost`
- `cat /etc/sysctl.conf`
- `sudo sysctl -p`
- `sysctl kernel.pid_max`, `cat /proc/sys/kernel/pid_max`, `cat &`, `sudo sysctl kernel.pid_max=24000`, `sudo sh -c 'echo 24000 > /proc/sys/kernel/pid_max'`, `cat /proc/sys/kernel/pid_max`, `cat &`

## Kernel Modules

- `lsmod`, `insmod`, `rmmod`, `modprobe`, `depmod`, `modinfo`
- `modprobe e1000e`, `modprobe -r e1000e`
- `depmod`
- `insmod /lib/modules/$(uname -r)/kernel/drivers/net/ethernet/intel/e1000.ko.xz` , `rmmod e1000`
- `sudo /sbin/insmod <pathto>/e1000e.ko debug=2 copybreak=256`, `sudo /sbin/modprobe e1000e debug=2 copybreak=256`, `cat /sys/module/e1000e/parameters`
- `ll /etc/modprobe.d`
- `cd /lib/modules/5.4.0-73-generic/kernel/drivers/net/ethernet/3com/`, `sudo modprobe 3c509`, `lsmod | head`, `sudo modprobe -r 3c509`, `lsmod | head`, `dmesg | tail -30`
- `lsmod`, `sudo insmod /lib/modules/$(uname -r)/kernel/drivers/net/ethernet/intel/e100`, `sudo /sbin/modprobe e100`, `lsmod | grep e100`, `sudo rmmod e100`, `sudo modprobe -r e100`, `lsmod | grep e100`

## Devices and udev

- `ls -l /dev`
- `sudo mknod [-m mode] /dev/name <type> </major> <minor>`: `sudo mknod -m 666 /dev/mycdrv c 254 1`
- `ll /etc/udev/rules.d/`, `cat /etc/udev/rules.d/<rulename>.rules`
- `/etc/udev/rules.d`, `/run/udev/rules.d`, `/usr/lib/udev/rules.d`
- `man udev`, `SYMLINK`, `RUN`
- `cat /usr/lib/udev/rules.d/99-fitbit.rules`, `SUBSYSTEM=="usb", ATTR{idVendor}=="2687", ATTR{idProduct}=="fb01", SYMLINK+="fitbit", MODE="0666"`
- `cat /usr/lib/udev/rules.d/98-kexec.rules`, `SUBSYSTEM=="cpu", ACTION=="add", PROGRAM="/bin/systemctl try-restart kdump.service"`, `SUBSYSTEM=="cpu", ACTION=="remove", PROGRAM="/bin/systemctl try-restart kdump.service"`, `SUBSYSTEM=="memory", ACTION=="online", PROGRAM="/bin/systemctl try-restart kdump.service"`, `SUBSYSTEM=="memory", ACTION=="offline", PROGRAM="/bin/systemctl try-restart kdump.service"`
- `cat /usr/lib/udev/rules.d/80-kvm.rules`, `KERNEL=="kvm", GROUP="kvm", MODE="0666"`
- `stat --help`, `mknod --help`
- `se /etc/udev/rules.d/75-myusb.rules`, `SUBSYSTEM=="usb", SYMLINK+="myusb"`, `ls -lF /dev | grep myusb`, `umount /media/whatever`, `ls -lF /dev | grep myusb`

## Virtualization

- `sudo apt-get install qemu`, `qemu-img --help | grep formats:`, `qemu-img convert -O vmdk myvm.qcow2 myvm.vmdk`
- `grep -e vmx -e svm /proc/cpuinfo`
- `sudo dnf|zypper install kvm* qemu* libvirt*`
- `sudo systemctl stop vmware` ,`sudo systemctl stop vboxdrv`
- `sudo systemctl status libvirtd`, `sudo virt-manager`
- `sudo qemu-img create -f qcow2 somedir/myimg.qcow2 24M`, `sudo qemu-system-x86_64 -hda somedir/myimg.qcow2 -cdrom ./os.iso  -usbdevice tablet`

## Containers

- `docker`, `docker-search`, `docker-pull`, `docker-create`, `docker-run`
- `docker <command> --help`
- `docker rm $(docker ps -a -q)`
- `sudo apt-get update`, `sudo apt-get install software-properties-common`, `sudo add-apt-repository ppa:projectatomic/ppa`, `sudo apt-get update`, `sudo apt-get install podman`
- `sudo yum install docker`, `sudo dnf install podman podman-docker`
- `sudo apt-get install docker.io`
- `sudo zypper install docker`
- `sudo systemctl start docker`, `systemctl status docker`
- `sudo docker search apache`, `sudo docker pull docker.io/httpd`, `sudo docker images`, `sudo  docker images --all`, `sudo docker run httpd`, `lynx   http://172.17.0.2`, `w3m    http://172.17.0.2`, `elinks http://172.17.0.2`, `sudo docker ps`, `sudo docker stop hexid`, `sudo docker rmi -f docker.io/httpd`, `sudo docker system prune -a`, `sudo systemctl stop docker`

## User account management

- `sudo useradd dexter`
- `sudo useradd -s /bin/csh -m -k /etc/skel -c "Bullwinkle J Moose" bmoose`
- `sudo userdel morgan`
- `sudo usermod -L dexter`, `sudo usermod -U dexter`, `sudo chage -E 2014-09-11 morgan`
- `sudo usermod --help`
- `cat /etc/passwd`, `cat /etc/shadow`, `/etc/login.defs`, `/etc/group`
- `passwd`, `sudo passwd kevin`
- `chage [-m mindays] [-M maxdays] [-d lastday] [-I inactive] [-E expiredate] [-W warndays] user`
- `sudo chage -l stephane`, `sudo chage -m 14 -M 30 kevlin`, `sudo chage -E 2012-4-1 isabelle`, `sudo chage -d 0 clyde`
- `bash -r`, https://www.metahackers.pro/breakout-of-restricted-shell/, https://www.exploit-db.com/docs/english/44592-linux-restricted-shell-bypass-guide.pdf
- `sudo grep student /etc/passwd /etc/shadow`, `sudo useradd user1`, `ssh user1@localhost`, `sudo service sshd restart`, `sudo systemctl restart sshd.service`, `sudo passwd user1`, `sudo grep user1 /etc/passwd /etc/shadow`, `cat /etc/default/useradd`, `cat /etc/login.defs`, `sudo useradd -s /bin/ksh user2`, `sudo passwd user2`, `sudo grep user1 /etc/shadow`, `sudo chage -E 2013-12-1 user1`, `sudo grep user1 /etc/shadow`, `sudo usermod -L user1`, `sudo passwd user1`
- `bash -r`, `cd $HOME`, `PATH=$PATH:/tmp`, `exit`, `sudo ln /bin/bash /bin/rbash`, `sudo useradd -s /bin/rbash fool`, `sudo passwd fool`, `sudo su - fool`, `cd /tmp`, `PATH=$PATH:/tmp`, `exit`, `sudo userdel -r fool`, `sudo rm /bin/rbash`

## Group management

- `groupadd`, `groupdel`, `groupmod`, `usermod`
- `/etc/group`
- `sudo groupadd -r -g 215 staff`
- `sudo groupmod -g 101 blah`
- `sudo groupdel newgroup`
- `sudo usermod -G student,group1,group2 student`
- `sudo useradd -m rocky`, `sudo useradd -m bullwinkle`, `sudo passwd rocky`, `sudo passwd bullwinkle`, `ls -l /home`, `sudo groupadd friends`, `sudo groupadd -g 490 bosses`, `grep -e friends -e bosses /etc/group`, `sudo usermod -G friends,bosses rocky`, `sudo usermod -G friends bullwinkle`, `grep -e rocky -e bullwinkle /etc/group`, `groups rocky bullwinkle`, `ssh rocky@localhost`, `cd ~`, `mkdir somedir`, `chgrp bosses somedir`, `ls -l`, `chmod a+x .`, `ssh bullwinkle@localhost`, `touch /home/rocky/somedir/somefile`, `exit`, `sudo usermod -a -G bosses bullwinkle`, `ssh bullwinkle@localhost`, `touch /home/rocky/somedir/somefile`, `ls -al /home/rocky/somedir`

## File Permissions and ownership

- `chmod`, `chown`, `chgrp`, `umask`
- `chmod uo+x,g-w a_file`
- `sudo chown wally somefile`
- `sudo chgrp cleavers somefile`
- `sudo chown wally:cleavers somefile`
- `sudo chown -R wally:cleavers ./`
- `sudo chown -R wally:wally subdir`
- `umask 0022`, `umask u=r,g=w,o=rw`, `umask -S`
- `sudo apt install acl`
- `getfacl /home/ubuntu/`
- `setfacl -m u:isabelle:rx /home/stephane/file1`
- `setfacl -x u:isabelle /home/stephane/file`
- `setfacl -m d:u:isabelle:rx somedir`
- `chmod u=r,g=w,o=x afile`, `chmod u+w,g-w,o+rw afile`, `chmod ug=rwx,o-rw afile`, `ls -l afile`
- `touch afile`, `ls -l afile`, `umask`, `umask 0022`, `touch afile2`, `umask 0666`, `touch afile3`, `ls -l afile*`
- `echo This is a file > /tmp/afile`, `getfacl /tmp/afile`, `sudo useradd fool`, `sudo passwd fool`, `sudo su - fool`, `echo another line > /tmp/afile`, `setfacl -m u:fool:rw /tmp/afile`, `getfacl /tmp/afile`, `echo another line > /tmp/afile`, `setfacl -m u:fool:w /tmp/afile`, `echo another line > /tmp/afile`, `rm /tmp/afile`, `sudo userdel -r fool`

## Pluggable authentication modules

- `/etc/pam.d`

## Network addresses

- https://en.wikipedia.org/wiki/Reserved_IP_addresses
- `hostname`
- `sudo hostname lumpy`
- `sudo hostnamectl set-hostname lumpy`
- `/etc/sysconfig/network`, `/etc/hostname`, `/etc/HOSTNAME`
- `hostnamectl`, `hostnamectl --help`

## Network devices and configuration

- `ip`, `ifconfig`, `nmtui`, `nmcli`, `/etc`
- `ip [ OPTIONS ] OBJECT { COMMAND | help }`, `ip [ -force ] -batch filename`
- `ip`: `address`, `link`, `maddress`, `monitor`, `route`, `rule`, `tunnel`
- `ip link show`, `ip -s link show eth0`, `sudo ip addr add 192.168.1.7 dev eth0`, `sudo ip link set eth0 down`, `sudo ip link set eth0 mtu 1480`, `sudo ip route add 172.16.1.0/24 via 192.168.1.5`
- `ifconfig`, `ifconfig eth0`, `sudo ifconfig eth0 192.168.1.50`, `sudo ifconfig eth0 netmask 255.255.255.0`, `sudo ifconfig eth0 up`, `sudo ifconfig eth0 down`, `sudo ifconfig eth0 mtu 1480`
- `ip link show | grep enp`, `ifconfig | grep enp`, `lspci | grep Ethernet`
- `ip link show | grep wl`, `lspci | grep Centrino`
- Red Hat: `/etc/sysconfig/network`, `/etc/sysconfig/network-scripts/ifcfg-ethX`, `/etc/sysconfig/network-scripts/ifcfg-ethX:Y`, `/etc/sysconfig/network-scripts/route-ethX`
- Debian: `/etc/network/interfaces`
- Suse: `/etc/sysconfig/network`
- `man nmcli-examples`
- `route -n`, `ip route`
- `sudo nmcli con mod virbr0 ipv4.routes 192.168.10.0/24 +ipv4.gateway 192.168.122.0`, `sudo nmcli con up virbr0`
- `/etc/sysconfig/network`, `GATEWAY=x.x.x.x`, `/etc/sysconfig/network-scripts/ifcfg-ethX`
- `/etc/network/interfaces`, `gateway=x.x.x.x`
- `sudo route add default gw 192.168.1.10 enp2s0`, `route`, `sudo route add default gw 192.168.1.1 enp2s0`
- `sudo ip route add 10.5.0.0/16 via 192.168.1.100`
- Red Hat: `cat /etc/sysconfig/network-scripts/route-eth0`
- Debian: `/etc/network/interfaces`, `iface eth1 inet dhcp`, `post-up route add -host 10.1.2.51 eth1`, `post-up route add -host 10.1.2.52 eth1`
- Suse: `/etc/sysconfig/network/ifroute-eth0`, `192.168.1.150 192.168.1.1 255.255.255.255 eth0`, `10.1.1.150 192.168.233.1.1 eth0`, `10.1.1.0/24 192.168.1.1 - eth0`
- `[dig | host | nslookup] linuxfoundation.org`
- `/etc/hosts`, `/etc/hosts.deny`, `/etc/hosts.allow`, (`/etc/host.conf`, `/etc/nsswitch.conf`)
- `/etc/resolv.conf`
- `ping -c 10 linuxfoundation.org`, `traceroute linuxfoundation.org`, `mtr linuxfoundation.org`
- `ip addr show eth0`, `ip route`, `cp /etc/resolv.conf resolv.conf.keep`, `ifconfig eth0`, `route -n`, `cp /etc/resolv.conf resolv.conf.keep`, `sudo ip link set eth0 down`, `sudo ifconfig eth0 down`; Red Hat: `/etc/sysconfig/network-scripts/ifcfg-eth0`, `DEVICE=eth0`, `BOOTPROTO=static`, `ONBOOT=yes`, `IPADDR=noted from step1`, `NETMASK=noted from step1`, `GATEWAY=noted from step1`; Suse: `/etc/sysconfig/network`, `iface eth0 inet static`, `address noted from step1`, `netmask noted from step1`, `gateway noted from step1`; Debian: `/etc/networking/interfaces`, `sudo ip link set eth0 up`, `sudo ifconfig eth0 up`, `sudo cp resolv.conf.keep /etc/resolv.conf`, `cat /etc/sysconfig/network`, `cat /etc/hosts`, `ping yourhostname`, `sudo reboot`, `ping hostname`
- `/etc/hosts`, `sudo sh -c "echo 192.168.1.180    mysystem.mydomain >> /etc/hosts"`, `ping mysystem.mydomain`, `sudo sh -c "echo 127.0.0.1       ad.doubleclick.net >> /etc/hosts"`, `ping ad.doubleclick.net`, `wget http://winhelp2002.mvps.org/hosts.txt`, `sudo sh -c "cat hosts.txt >> /etc/hosts"`
- `sudo nmcli con`, `sudo nmcli con show "Auto Ethernet" | grep IP4.ADDRESS`, `nmcli con show 1c46bf37-2e4c-460d-8b20-421540f7d0e2`, `sudo nmcli con modify "Auto Ethernet" +ipv4.addresses 172.16.2.140/24`, `sudo nmcli con up "Auto Ethernet"`, `sudo nmcli con modify  "Auto Ethernet" -ipv4.addresses 172.16.2.140/24`, `sudo nmcli con up "Auto Ethernet"`
- `route`, `ip route`, `sudo nmcli conn mod "Auto Ethernet" +ipv4.routes "192.168.100.0/24 172.16.2.1"`, `route`, `sudo nmcli conn up "Auto Ethernet"`, `route`, `reboot`, `route`, `sudo nmcli conn mod "Auto Ethernet" -ipv4.routes "192.168.100.0/24 172.16.2.1"`, `sudo nmcli conn up "Auto Ethernet"`, `sudo ip route add 192.168.100.0/24 via 172.16.2.1`, `sudo route`

## Firewalls

- `iptables`, `firewall-cmd`, `ufw`
- `system-config-firewall`, `firewall-config`, `gufw`, `yast`
- `/etc/firewalld`, `/usr/lib/firewalld`, `firewall-cmd --help`
- `sudo systemctl [enable/disable] firewalld`, `sudo systemctl [start/stop] firewalld`, `sudo systemctl status firewalld`
- `sudo firewall-cmd --state`
- `sudo sysctl net.ipv4.ip_forward=1`, `echo 1 > /proc/sys/net/ipv4/ip_forward`
- `sudo sysctl -p`
- `sudo firewall-cmd --get-default-zone`, `sudo firewall-cmd --get-active-zones`, `sudo firewall-cmd --get-zones`, `sudo firewall-cmd --set-default-zone=trusted`, `sudo firewall-cmd --set-default-zone=public`, `sudo firewall-cmd --zone=internal --change-interface=eno1`, `sudo firewall-cmd --permanent --zone=internal --change-interface=eno1` (`/etc/firewalld/zones/internal.xml`), `sudo firewall-cmd --get-zone-of-interface=eno1`, `sudo firewall-cmd --zone=public --list-all`
- `sudo firewall-cmd --permanent --zone=trusted --add-source=192.168.1.0/24`, `sudo firewall-cmd --permanent --zone=trusted --list-sources`
- `sudo firewall-cmd --get-services`, `sudo firewall-cmd --list-services --zone=public`, `sudo firewall-cmd --permanent --zone=home --add-service=dhcp`, `sudo firewall-cmd --reload`, `/etc/firewalld/services`
- `sudo firewall-cmd --zone=home --add-port=21/tcp`, `sudo firewall-cmd --zone=home --list-ports`, `grep "21/tcp" /etc/services`
- `tar xvf firewalld-0.3.13.tar.bz2`, `cd firewalld-0.3.13`, `./configure`, `make`, `sudo make install`, `sudo make uninstall`
- `man firewall-cmd`, `man firewalld`
- `sudo firewall-cmd  --zone=public --add-service=http`, `sudo firewall-cmd  --zone=public --add-service=https`, `sudo firewall-cmd --list-services --zone=public`, `sudo firewall-cmd --reload`, `sudo firewall-cmd --list-services --zone=public`

## System startup and shutdown

- `/usr/lib/systemd`, `/etc/systemd`
- Red Hat: `/etc/sysconfig`, `/etc/sysconfig/selinux`
- Debian: `/etc/default`, `/etc/default/useradd`
- `shutdown -h +1 "Power Failure imminent"`, `shutdown -h now`, `shutdown -r now`, `shutdown now`, `/sbin/shutdown --help`, `reboot`, `halt`, `poweroff`

## Grub

- `/boot/grub/grub.cfg`, `/boot/grub2/grub.cfg`, `/boot/efi/EFI/redhat/grub.cfg`
- `update-grub`, `grub2-mkconfig`
- `/etc/default/grub`, `/etc/grub.d`
- `sudo grub2-install /dev/sda`
- `efibootmgr`
- `/boot/loader/entries`, `/boot/grub2/grubenv`
- `e`, ` 3`, `C-x`, `sudo systemctl start gdm`, `sudo systemctl start lightdm`, `sudo telinit 5`, `sudo service gdm restart`, `sudo service lightdm restart`
- https://systemd.io/BOOT_LOADER_SPECIFICATION/ 

## System init: systemd, systemv and upstart

- `/etc/hostname`, `/etc/vconsole.conf`, `/etc/sysctl.d/*.conf`, `/etc/os-release`
- `systemctl [options] command [name]`
- `systemctl`
- `systemctl list-units -t service --all`
- `systemctl list-units -t service`
- `sudo systemctl start foo`
- `sudo systemctl start foo.service`
- `sudo systemctl start /path/to/foo.service`
- `sudo systemctl stop foo.service`
- `sudo systemctl enable sshd.service`
- `sudo systemctl disable sshd.service`
- https://fedoraproject.org/wiki/SysVinit_to_Systemd_Cheatsheet
- `sudo systemctl start fake.service`, `sudo systemctl status fake.service`, `sudo systemctl stop fake.service`, `sudo systemctl daemon-reload`, `sudo tail -f /var/log/messages` (`/var/log/syslog`), `sudo systemctl enable fake.service`, `sudo systemctl disable fake.service`

## Backup and recovery methods

- `cpio`, `tar`
- `gzip`, `bzip2`, `xz`
- `dd`
- `rsync`
- `dump`, `restore`
- `mt`
- `tar cvf  /dev/st0 /root`, `tar -cvf /dev/st0 /root`
- `tar -cMf /dev/st0 /root`
- `tar --compare --verbose --file /dev/st0`, `tar -dvf /dev/st0`
- `
- `
- `
- `
- `
- `
- `
- `
- `
- `
- `
- `
- `
- `
- `

## Linux security modules

- `
- `
- `
- `
- `
- `
- `
- `
- `
- `

## Local system security

- `
- `
- `
- `
- `
- `
- `
- `
- `
- `
- `
- `

## Basic troubleshooting

- `
- `
- `
- `
- `
- `
- `
- `
- `
- `

## System rescue

- `
- `
- `
- `
- `
- `
- `
- `
- `
- `

<!------ L2 ------>

# L2

## Linux networking: concept and review

## Network configuration

## Network troubleshooting and monitoring

## Remote access

## Domain name service

## Http servers

## Advanced http servers

## Email servers

## File sharing 

## Advanced networking

## Http caching

## Network file systems

## Network security

## Firewalls

## LXC virtualization

## High availability

## Databases

## System log

## Package management


