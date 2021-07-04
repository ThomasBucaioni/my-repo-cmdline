# L0

# DevOps

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
- `

## User account management

## Group management

## File Permissions and ownership

## Pluggable authentication modules

## Network addresses

## Network devices and configuration

## Firewalls

## System startup and shutdown

## Grub

## System init: systemd, systemv and upstart

## Backup and recovery methods

## Linux security modules

## Local system security

## Basic troubleshooting

## System rescue

# L2

