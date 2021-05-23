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
- `
