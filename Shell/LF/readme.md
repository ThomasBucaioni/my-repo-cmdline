# L0

## OSS projects

- https://www.kernel.org/
- https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
- https://www.apache.org/
- https://httpd.apache.org/
- https://www.apache.org/licenses/
- https://www.openstack.org/
- https://kubernetes.io/
- https://www.onap.org/
- https://www.hyperledger.org/
- https://nodejs.org/en/
- https://xenproject.org/
- https://www.coreinfrastructure.org/
- https://www.automotivelinux.org/

## Continuous integration

- https://www.jenkins.io/
- https://jenkins-x.io/
- https://spinnaker.io/
- https://cloud.google.com/tekton/
- https://www.linuxfoundation.org/press-release/2019/03/the-linux-foundation-announces-new-foundation-to-support-continuous-delivery-collaboration/
- https://cd.foundation/
- https://stackify.com/top-continuous-integration-tools/
- https://travis-ci.org/
- https://www.jetbrains.com/teamcity/
- https://www.gocd.org/
- https://about.gitlab.com/stages-devops-lifecycle/continuous-integration/
- https://www.atlassian.com/software/bamboo
- https://www.cloudbees.com/products/codeship
- https://circleci.com/
- https://kernelci.org/
- https://www.linaro.org/
- https://foundation.kernelci.org/
- https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses
- https://openinventionnetwork.com/
- http://oss-watch.ac.uk/apps/licdiff/
- https://opensource.org/licenses/category
- https://choosealicense.com/
- https://tldrlegal.com/licenses/browse
- https://www.gnu.org/licenses/license-list.en.html
- https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#SoftwareLicenses
- https://wiki.debian.org/DFSGLicenses
- https://source.android.com/setup/start/licenses
- https://www.apache.org/legal/resolved.html

## GitHub

- https://about.gitlab.com/
- https://www.gitkraken.com/
- https://launchpad.net/

## Linux and the operating system

- https://askubuntu.com/questions/161511/are-the-linux-utilities-parts-of-the-kernel-shell
- https://www.linuxfoundation.org/
- https://lwn.net/Distributions/
- https://distrowatch.com/
- https://wiki.linuxfoundation.org/lsb/start

## Graphical environments and interfaces

- https://www.x.org/wiki/
- https://wayland.freedesktop.org/

## System administration

- https://fedoraproject.org/wiki/EPEL

## Text editors

- https://www.openvim.com/

## Shell, bash and the command line

- `/etc/profile`, `~/.bash_profile`, `~/.bash_login`, `~/.profile`, `~/.bash_logout`, `~/.bashrc`
- `>&`, `2>&1`: `foo &> file` = `foo > file 2>&1`
- `alias diffside='diff --side-by-side --ignore-all-space'`
- `PAGER=/usr/bin/less`, `NCPUS=$(grep ˆprocessor /proc/cpuinfo | wc -l)`
- `PS1="\h:\u:\w>"`, `\t`, `\d`, `\n`, `\s`, `\w`, `\W`, `\u`, `\h`, `\#`, `\!`
- `\#>` (Default # = 1, stdout)
- `foobar 2>&1 | tee filename`
- `ls -l ``which --skip-alias emacs`` `, `ls -l $(which --skip-alias emacs)`

## Filesystem layout

- https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf
- `sudo /sbin/fdisk -l`
- `sudo mkfs -t ext4 /dev/sda10`, `sudo mkfs.ext4 /dev/sda10`

### Paths

- `echo $PATH`
- `which --skip-alias emacs`
- `export CDPATH=/usr:$CDPATH`, `cd bin`

### Hard and soft links

- `ln file1 file2`, `ls -li file1 file2`, `ls -li /bin/g*zip`
- `ln -s file1 file2`, `ls -li file1 file2`
- `symlinks -rv /etc`

## System boot

- `/boot/grub/grub.cfg`, `/boot/grub2/grub.cfg`
- `/etc/grub.d`, `/etc/default/grub`
- `/boot/efi/EFI/redhat/grub.cfg`
- `vmlinuz`, `initramfs`, `config`, `System.map`
- `/sbin/init`
- `sudo systemctl stop gdm`, `sudo systemctl start gdm`

## Memory

- `free -mt`
- `sudo su`, `echo 3 > /proc/sys/vm/drop_caches`, `free -mt`
- `cat /proc/meminfo`
- http://people.redhat.com/drepper/cpumemory.pdf
- `cat /proc/swaps`
- `mkswap`, `swapon`, `swapoff`
- `clone()`, `pthread_create()`



## Networking

- `ip -s link`, `ifconfig`
- `ls -l /sys/class/net/eno1/statistics`
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

- https://fedoraproject.org/wiki/SysVinit_to_Systemd_Cheatsheet
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
- `find /tmp -newer /tmp/tstfile -ls`, `find /etc -name "*.conf"`, `find /etc -type d`, `find / -name "*.bak" -exec rm {} ';'`

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
- `grep ftp /etc/services | grep tcp`, `grep -n ftp /etc/services | grep -v tcp`, `grep'ˆts'/etc/services`, `grep'st$'/etc/services`

#### Command `sed`

- `sed s/pig/cow/ file > newfile`
- `sed s/pig/cow/ < file > newfile`
- `cat file | sed s/pig/cow/ > newfile`
- `sed s/pig/cow/g file > newfile`
- `sed s:pig:cow:g file > newfile`
- `sed s/'\\'/'\/'/g file > newfile` ++
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

- `$0`, `$1`, `$2`, `$*`, `$@`, `$#`: `man bash`
- `shift n`
- `. file`, `source file`
- `set -n` (`bash -n`), `set -x` (`bash -x`), `set -v` (`bash -v`), `set -u` (`bash -u`), `set -e` (`bash -e`)
- `set +n` (`bash +n`), `set +x` (`bash +x`), `set +v` (`bash +v`), `set +u` (`bash +u`), `set +e` (`bash +e`)
- `man set`

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

```
#!/bin/sh
echo "Do you want to destroy your entire file system?
read response
case "$response" in
  "yes") echo "I hope you know what you are doing!" ;;
  "no" ) echo "You have some comon sense!" ;;
  "y" | "Y" | "YES" ) echo "I hope you know what you are doing!" ;
     echo 'I am going to type: " rm -rf /"';;
  "n" | "N" | "NO" ) echo "You have some comon sense!" ;;
  * ) echo "You have to give an answer!" ;;
esac
exit 0
```

### Loops

#### For

- `for file in $(find . -name "*.o")`, `do`, `echo "I am removing file: $file"`, `rm -f "$file"`, `done`
- `find . -name "*.o" -exec rm {} ';'`
- `find . -name "*.o" | xargs rm`

#### While

```
​#!/bin/sh
ntry_max=4 ; ntry=0 ; password=' '
while [[ $ntry -lt $ntry_max ]] ; do
  ntry=$(( $ntry + 1 ))
  echo -n 'Give password:  '
  read password
  if  [[ $password == "linux" ]] ; then
    echo "Congratulations: You gave the right password on try $ntry!"
    exit 0
  fi
  echo "You failed on try $ntry; try again!"
done
echo "you failed $ntry_max times; giving up"
exit -1
```

#### Until

```
#!/bin/sh
ntry_max=4 ; ntry=0 ; password=' '
until [[ $ntry -ge $ntry_max ]] ; do
  ntry=$(( $ntry + 1 ))
  echo -n 'Give password:  '
  read password
  if [[ $password == "linux" ]] ; then
    echo "Congratulations: You gave the right password on try $ntry!"
    exit 0
  fi
  echo "You failed on try $ntry; try again!"
done
echo "you failed $ntry_max times; giving up"
exit -1
```

### Functions

```
#!/bin/sh
test_fun1(){
var=FUN_VAR
shift
echo " PARS after fun shift: $0 $1 $2 $3 $4 $5"
}
var=MAIN_VAR
echo ' '
echo "BEFORE FUN MAIN, VAR=$var"
echo " PARS starting in main: $0 $1 $2 $3 $4 $5"
test_fun1 "$@"
echo " PARS after fun in main: $0 $1 $2 $3 $4 $5"
echo "AFTER FUN MAIN, VAR=$var"
exit 0
```

```
function fun_foobar(){
statements
}
function fun_foobar{
statements
}
```
(not in sh)

### Examples

#### Simple bash script

```
#!/bin/sh
nproc=$(ps | wc -l)
echo "You are running $nproc processes"
exit 0
```

#### Simple backup script

```
#!/bin/sh
usage="Usage: Backup Source Target"
if [[ $# -lt 2 ]] ; then
  echo -e '\n'    $usage '\n'
  exit 1 
fi
if ! [[ -d $1 ]] ; then
  echo -e '\n' ERROR: First argument must be a Directory that exists: quitting'\n'
  exit 1
fi
SOURCE=$1
TARGET=$2
DIRLIST=$(cd $SOURCE ; find . -type d )
for NAMES in $DIRLIST
do
  SOURCE_DIR=$SOURCE/$NAMES
  TARGET_DIR=$TARGET/$NAMES
  echo "SOURCE= $SOURCE_DIR      TARGET=$TARGET_DIR"
  FILELIST=$( (cd $SOURCE_DIR ; find . -maxdepth 1 ! -type d ) )
  mkdir -p $TARGET_DIR
  OLDIFS=$IFS
  IFS=''
  tar -zcvf $TARGET_DIR/Backup.tar.gz  -C $SOURCE_DIR $FILELIST
  IFS=$OLDIFS
done
```

## Files and filesystem

- `ls -lF`, `-`, `d`, `l`, `p`, `s`, `b`, `c`
- `file *`
- `ls -l a_file`
- `chmod uo+x,g-w a_file`, `chmod 755 a_file`
- `chgrp aproject a_file`
- `chown coop a_file`, `chown coop.aproject a_file`, `chown -R coop.aproject .`, `chown -R coop.aproject subdir`
- `umask`, `umask 0022`, `umask -S`, `umask u=r,g=w,o=rw`
- `sudo chmod +s a.out`

## Compiling, linking, and libraries


- http://gcc.gnu.org/
- https://clangbuiltlinux.github.io/
- https://software.intel.com/content/www/us/en/develop/tools/oneapi/all-toolkits.html#gs.8sct28
- https://software.intel.com/content/www/us/en/develop/articles/free-intel-software-developer-tools.html
- `gcc`, `-Idir`, `-Ldir`, `-l`, `-M`, `-H`, `-E`, `-D def`, `-U def`, `-d`, `-v`, `-pedantic`, `-w`, `-W`, `-Wall`, `-g`, `-pg`, `-c`, `-o file`, `-x lang`, `-ansi`, `-pipe`, `-static`, `-O[lev]`, `-Os`, `-O2 -Wall -pedantic`
- `ar rv libsubs.a *.o`, `ranlib libsubs.a`, `nm -s libsubs.a`
- `gcc -fPIC -c func1.c`, `gcc -fPIC -c func2.c`, `gcc -fPIC -shared -Wl,-soname=libmyfuncs.so.1 *.o -o libmyfuncs.so.1.0 -lc`, `ld -shared -soname=libmyfuncs.so.1 *.o -o libmyfuncs.so.1.0 -lc`, `ln -s libmyfuncs.so.1.0 libmyfuncs.so`, `ln -s libmyfuncs.so.1.0 libmyfuncs.so.1`
- `info libtool`
- `ldd`, `ldconfig`, `/etc/ld.so.conf`, `ldd /usr/bin/vi`
- `LD_LIBRARY_PATH=$HOME/foo/lib ; foo [args]`, `LD_LIBRARY_PATH=$HOME/foo/lib foo [args]`
- `gcc -o foo foo.c -L/mypath/lib -lfoolib`, `/mypath/lib/libfoolib.so`, `/mypath/lib/libfoolib.a`
- `info gcc`, `gcc --print-search-dirs`, `/usr/lib`, `/lib`
- `strip foobar`
- `LD_DEBUG=help`
- `gdb`, `.gdbinit`
- https://www.eclipse.org/
- https://www.gnu.org/software/ddd/
- `ldd /usr/bin/vim`, `vim &`, `cat /proc/pid/maps`, `pmap -d 2 pid`

## Java intallation and environment

- https://www.oracle.com/java/technologies/javase-downloads.html
- https://www.ibm.com/support/pages/java-sdk-downloads
- `sudo dnf install java-1.8.0-openjdk`, `sudo dnf install java-1.8.0-openjdk-devel`
- `sudo apt-get install default-jre default-jdk`, `sudo apt-get install openjdk-8-jre openjdk--jdk`
- `sudo alternatives --config java`, `ls -l /etc/alternatives/java`, `which java`, `ls -l /usr/bin/java`, `sudo alternatives --config javac`, `export JAVA_HOME=/usr/lib/jvm/java-1.6.0-sun-1.6.0.21.x86_64/jre`, `export PATH=$JAVA_HOME/bin:$PATH`, `java -version`
- `readlink -f $(which java)`, `CLASSPATH`
- `sudo apt-get install netbeans`
- https://netbeans.apache.org//

## Building RPM and Debian packages

- `rpm -qil rpm-build | grep bin`
- `rpm -qil rpm | grep bin`
- `rpmbuild -ba specFile`
- `rpmbuild --rebuild SourceRPM`
- `rpm -i data`
- `rpm -qi package`
- `rpm -qR package`
- `rpm -q --provides gzip`
- `find-requires`, `find-provides`, `requires: package`, `requires: package >= version`, `requires: package >= version-build`
- https://www.debian.org/doc/manuals/maint-guide/
- `debuild`, `cdbs`
- `

## Git

### Available revision control systems

- https://www.gnu.org/software/rcs/
- http://savannah.nongnu.org/projects/cvs
- https://subversion.apache.org/
- https://mirrors.edge.kernel.org/pub/software/scm/git/
- http://bazaar.canonical.com/en/
- https://www.monotone.ca/
- https://www.mercurial-scm.org/
- http://prcs.sourceforge.net/

### Graphical interfaces

- `git-gui`, `gitk`, `cgit`, `gitweb`

### Books and online resources

- https://mirrors.edge.kernel.org/pub/software/scm/git/docs/user-manual.html
- Loeliger, J. & McCullough, M. (2012). Version control with Git: Powerful tools and techniques for collaborative software development (2nd ed.). Sebastopol, CA: O'Reilly Media, Inc.
- https://git-scm.com/
- https://training.linuxfoundation.org/cm/prep/talks/ESC.pdf
- https://training.linuxfoundation.org/resources/webinars/introduction-to-git/

### Cgit example

- cgit: https://git.kernel.org
- not cgit: https://www.kernel.org

## Installation

- `which git`, `/usr/bin/git`
- `sudo [dnf|yum] list git*`, `sudo [dnf|yum] install git* cgit`
- `sudo zypper search git`, `sudo zypper install git git-core`
- `sudo apt-get install git-core git-gui gitweb cgit gitk git-daemon-run git-cvs git-svn gettext`
- `sudo emerge -a dev-util/git`
- https://cygwin.com/
- https://gitforwindows.org/
- `git clone -v https://github.com/git/git.git`, `cd git`, `./configure`, `make`, `sudo make install`; `make prefix=/usr`, `sudo make install`
- https://github.com/git/git
- https://git-scm.com/
- `git --version`
- `git tag`, `git log`
- `make prefix=/usr/local` or `make prefix=/opt`, `export PATH=/opt/bin:$PATH`

## Git and revision control systems

-https://www.bitkeeper.org/ `

### Converting between different systems

- `git svn clone  https://svn.apache.org/repos/asf/subversion/trunk/doc my_svn_repo`
- `svn log  https://svn.apache.org/repos/asf/subversion/trunk/doc | head`
- `git svn clone -rXYZ   https://svn.apache.org/repos/asf/subversion/trunk/doc my_svn_repo`
- `svn checkout https://svn.apache.org/repos/asf/subversion/trunk/doc doc`
- `diff -qr my_svn_repo/ doc/git.tex`

## An example

- `git --version`
- `git help [subcommand]`, `git help status`, `man git-status`, `git`, `git help --all`
- https://inclusivenaming.org/language/word-list/
- https://github.com/github/renaming
- `git init`
- `git checkout -b main`
- `git checkout master`, `git branch -m master main`, `git push -u origin main`, `git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main`, `git branch -a`
- `git checkout master`, `git branch main`, `git checkout main`, `git push -u origin main`
- `mkdir git-test`
- `cd git-test`
- `git init`
- `ls -l .git`
- `echo some junk > somejunkfile`
- `git add somejunkfile`
- `git status`
- `git config user.name "Another Genius"`
- `git config user.email "b_genius@linux.com"`
- `echo another line >> somejunkfile`
- `git diff`
- `git add somejunkfile`
- `git commit -m "My initial commit"`
- `git log`

## Concepts and architecture

- blobs

## Managing files and the index

- `.gitignore`
- `git add`, `git help add`, `-i`, `-u`
- `git rm`, `git rm myfile --cached`
- `git mv`, `git mv oldfile newfile` = `mv oldfile newfile ; git rm oldfile ; git add newfile`
- `git ls-files`, `git ls-files --others --exclude-standard`, `-t -c -o -s`,

## Commits

- `git commit file1`
- `git commit`, `git commit ./`, `git commit -a`
- `git diff`

### Identifiers and tags

- `git log | grep "^commit" | head -10`
- `git tag ver_10 longhexstring`, `git tag ver_10 shorthexstring`, `.git/refs/tags`

### Viewing the commit history

```
#!/bin/bash

rm -rf git-test
mkdir git-test

cd git-test
git init

git config user.name "A Smart Guy"
git config user.email "asmartguy@linux.com"

echo file1 > file1
git add file1
git commit file1 -m "This is the first commit"

echo file2 > file2
git add file2
git commit . -m "This is the second commit"

echo file3 > file3
echo another line for file3 >> file3
git add .
git commit . -m "This is the third commit"

echo another line for file2 >> file2
git add .
git commit -a -m "This is the fourth commit"
```
- `git log`
- `git log --pretty=oneline`
- `git log -p shorthexstring`
- `git help log`, `man git log`

### Reverting and resetting commits

- `git revert commit_name`, `HEAD`, `HEAD~`, `HEAD~~` = `HEAD~2`, `{hash number}`, `{tag name}`
- `git reset HEAD~2`, `--soft`, `--mixed`, `--hard`, `--merge`, `--keep`

### Tydying

- `du -shc .git`, `git gc`, `du -shc .git`
- `git prune -n`, `git prune`
- `git fsck`

### Blame

- `git blame file`, `git blame -L 3107,3121 kernel/sched/core.c​`

### Bisecting

- `git bisect start`, `git bisect bad`, `git bisect good mytag`
- `git bisect reset`
- `git bisect run ./myscript.sh`

## Branches

- `git branch [branch_name] [starting_point]`, `git/refs/heads`
- `git show-branch`
- `git branch devel`
- `git branch -d devel`

### Checkout

- `git checkout devel`, `git checkout main`, `.git/HEAD`
- `git checkout -b newbranch startpoint`

### Earlier file version

- `git show v1.1.1:src/myfile.c`
- `git checkout v1.1.1 src/myfile.c`

## Diffs

- `diff file1 file2`
- `diff -u file1 file2`
- `diff -Nur directory1 directory2`
- `git diff`
- `git diff earlier_commit`
- `git diff --cached earlier_commit`, `--staged`
- `git diff one_commit another_commit`, `--ignore-all-space`, `--stat`, `--numstat`
- `git diff v4.2.1 v4.2.2 Documentation/vm`
- `git diff --stat v4.2.1 v4.2.2 arch/x86_64`

## Merge

- `git checkout main`, `git merge devel`, `git status` ; `git merge devel`, `git ls-files`, `cat file`
- `git reset --hard main`
- `git checkout -b devel origin`, ..., `git checkout devel`, `git rebase main devel`, `git rebase --continue`
- `git rebase --abort`

## Repositories

- `git clone`
- `git pull`, `git fetch`
- `git push`
- `git clone git://git.kernel.org/pub/scm/git/git.git`, `file:///path/to/repo.git`, `ssh://user@remotesite.org[:port]/path/to/repo.git`, `user@remotesite.org:/path/to/repo.git`, `ht‌tp://remotesite.org/path/to/repo.git`, `ht‌tps://remotesite.org/path/to/repo.git`, `rsync://remotesite.org/path/to/repo.git`
- `--no-hardlinks`
- `git show-ref`
- `git ls-remote git://git.kernel.org/pub/scm/git/git.git`
- `git pull`

### Publishing

- `git clone --bare git-test /tmp/git-test`, `git clone /tmp/git-test my-git`
- `touch /tmp/git-test/git-daemon-export-ok`
- `git daemon &`
- `git clone 192.168.1.100:/tmp/git-test my-git`
- `git daemon --enable=receive-pack`, `[daemon] receivepack = true`
- `/var/www/html`, `/home/username/public_html`
- `git --bare update-server-info`
- `git clone https://192.168.1.100/git-test my-git`, `git clone https://192.168.1.100/~username/public_html`
- `git archive --verbose HEAD | bzip2 > myproject.tar.bz2`, `git archive --verbose v1.7.1 | bzip2 > myproject_v1.7.1.tar.bz2`
- https://www.saintsjd.com/2011/01/what-is-a-bare-git-repository/

### Fetching, pulling and pushing

- `git fetch ; git merge origin/main` = `git pull origin main`
- `git pull . branch`, `git merge branch`
- `git push git://remotesite.org/path/to/repo.git main`
- `git clone --bare <pathto>/git-test /tmp/my-remote-git-repo`, `git daemon`, `git clone git://ipaddress:/tmp/my-remote-git-repo`, `git daemon --base-path=/tmp`, `git clone git://ipaddress:/my-remote-git-repo`
- `git clone ssh://user@ipaddress:/tmp/my-remote-git-repo`, `git clone user@ipaddress:/tmp/my-remote-git-repo /tmp/my-remote-git-repo2`, `sudo dnf install openssh-server`, `sudo apt-get install openssh-server`

## Patches

- `diff -Nur stable_tree modified_tree > /path/to/my_patch`
- `diff -u original_file modified_file > /path/to/my_patch`
- `cd stable ; patch -p1 < /path/to/my_patch`
- `git format-patch -3`
- `git format-patch main`
- `git send-email -to linux-kernel@vger.kernel.org 0001-This-is-the-first-commit.patch`
- `git am 0002-This-is-the-second-commit.patch`
- `git am --resolved`
- `git am --skip`
- `git am --abort`
- `patch --dry-run < 0002-This-is-the-second-commit.patch`, `git add`, `git commit`
- `git apply --check 0002-This-is-the-second-commit.patch`, `git add`, `git commit`
```
rm -rf git-test ; mkdir git-test ; cd git-test
git init
git config user.name "A Smart Guy"
git config user.email "asmartguy@linux.com"
echo file1 > file1
echo file2 > file2
git add file1 file2
git commit . -m "This is our first commit"
cd ..
git clone git-test git-newer
cd git-newer
echo another line >> file2
echo a third file > file3
git add file2 file3
git commit -m"modifications from the new clone"
git format-patch -1 -s
mv 00* ..
cd ..
cd git-test
git apply --check ../00*
git am ../00*
```

## Gerrit

- https://gerrit-review.googlesource.com/Documentation/
- https://gerrit-review.googlesource.com/Documentation/intro-gerrit-walkthrough.html

<!------ DevOps ------>

# DevOps

## Docker

### Port cleaning

- `sudo lsof -i tcp:8080`, `sudo kill -9 PID`

<!------ L1 ------>

# L1

## Linux filesystem tree layout

- https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf
- `/`, `/bin`, `/boot` (kernel vmlinuz, initrd or initramfs), `/dev`, `/etc`, `/home`, `/lib`, `/lib64`, `/media`, `/mnt`, `/opt`, `/proc`, `/run`, `/sys`, `/root`, `/sbin`, `/srv`, `/tmp`, `/usr`, `/var`
- https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch03s17.html

### Disk space

- `ls -F`
- `sudo du -shxc --exclude=proc *`
- `file /usr/lib/zsh/5.8/zsh/*`
- `sudo du --max-depth=1 -hx /`
- https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf

### Proc filesystem

- `cd /proc`, `ls -F`
- `/proc/meminfo`
- `/proc/mounts`
- `/proc/cpuinfo`
- `/proc/swaps`
- `/proc/version`
- `/proc/partitions`
- `/proc/interrupts`

## Processes

### Controlling processes with ulimit

- `ulimit [options] [limit]`: `ulimit -n 1600`
- `ulimit -H -n`
- `ulimit -S -n`

### Using nice to set priorities

- `nice -n 5 command [ARGS]` = `nice 5 command [ARGS]`
- `nice cat &`, `ps -l`
- `renice --help`
- `renice +5 -p 20003`, `ps -lf`
- `gnome-system-monitor`

### Static and shared libraries

- `ls -l /usr/lib64/libpthread.*`, `libcrypt.*`
- `ldd /usr/bin/vi`
- `ldconfig`, `/etc/ld.so.conf`
- `LD_LIBRARY_PATH=$HOME/foo/lib ; foo [args]`, `LD_LIBRARY_PATH=$HOME/foo/lib foo [args]`

```
bash
ulimit -n
ulimit -S -n
ulimit -H -n
ulimit -n hard
ulimit -n
ulimit -n 2048
ulimit -n
ulimit -n 4096
ulimit -n
```

```
ipcs
ipcs -p
ps aux |grep -e pid1 -e pid2
```

## Signals

- `pkill [-signal] [options] [pattern]`
- `SIGKILL=9`, `SIGSTOP=19`, `SIGTERM=15`
- `kill -l`
- `man 7 signal`
- `killall`, `pkill`
- `kill pid`, `kill -SIGTERM pid`, `kill -9 pid`
- `pkill -HUP rsyslogd`

## Package management

- `# rpmbuild --rebuild -rb p7zip-16.02-16.el8.src.rpm`
- `# root/rpmbuild>find . -name "*rpm"`
- https://mirrors.edge.kernel.org/pub/software/scm/git/docs/
- `which git`, `git diff`, `git log`

### Rpm

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

### Dpkg

- `/var/lib/dpkg`
- `dpkg -l`
- `dpkg -s wget`
- `dpkg -S logrotate.conf`
- `dpkg -L logrotate`
- `dpkg -V logrotate`
- `sudo dpkg -i foobar.deb`
- `sudo dpkg -r logrotate`
- `sudo dpkg -P package`


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
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get -u upgrade
apt-cache search "kernel"
apt-cache search -n "kernel"
apt-cache pkgnames "kernel"
dpkg --get-selections "*kernel*"
sudo apt-get install apache2-dev
```
```
apt-cache search bash # search in name and description
apt-cache search -n bash # search installed or available (strict name)
apt-cache show bash # full description
apt-cache depends bash # dependencies
apt-cache rdepends bash # reverse dependencies
```
```
apt-cache search metapackage
sudo apt-get install bacula-client
```
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
- `sudo tail -f /var/log/messages`, `syslog`, `dmesg -w`, `boot.log`, `dmesg` , `secure`
- `cat /etc/logrotate.conf`
- `top`, `1`
- `vmstat -a 2 1000`
- https://wiki.ubuntu.com/Kernel/Reference/stress-ng
- `git clone git://kernel.ubuntu.com/cking/stress-ng.git`, `cd stress-ng`, `make`, `sudo make install`
- `stress-ng --help`, `info stress-ng`
- `stress-ng -c 8 -i 4 -m 6 -t 20s`, `stress-ng -m 4 -t 20s`

## Process Monitoring

- `ps aux`
- `ps -elf` ++
- `ps -eL`
- `ps -C "bash"`
- `ps -o pid,user,priority,cputime,pmem,size,command`
- `pstree -aAp process-id`, `-H`
- `ls -l /proc/process-id/task`
- `top`, `k`, `h`
```
ps -ef
ps aux
ps -o pid,pri,ni,cmd
bash
ps -o pid,pri,ni,cmd
nice -n 10 bash
renice 15 -p bash-process-id
ps -o pid,pri,ni,cmd
top
```
```
dd if=/dev/urandom of=/dev/null &
ps -C dd -o pid,cmd,stat
fg
^Z
ps -C dd -o pid,cmd,stat
jobs
fg
kill dd-pid
```

## Memory monitoring

- `cat /proc/meminfo`
- `ls /proc/sys/vm`
- `vmstat 2 4`, `vmstat -a 2 4`, `vmstat -SM -a 2 4`
- https://lwn.net/Articles/104185/
- `cat /proc/sys/vm/overcommit_memory`, `/proc/sys/vm/overcommit_ratio`
- `cat /proc/[pid]/oom_score`
```
sudo /sbin/swapoff -a
stress-ng -m 12 -t 10s
sudo /sbin/swapon -a
```

## I/O Monitoring

- `iostat`, `iotop`, `ionice`
- `iostat`, ` -k`, `-m`, `-N`, `-d`, `-xk`
- `iotop -o`
- `ionice -c 2 -n 3 -p [pid]`
```
iostat -m /dev/sda /dev/sdb 2 200
iotop -o
for names in */*.vmdk ; do /bin/cp $names /tmp/junk ; done
```
```
time sudo bonnie++ -n 0 -u 0 -r 100 -f -b -d /mnt
bon_csv2txt < bonnie++.out > bonnie++.txt
bon_csv2html < bonnie++.out > bonnie++.html
```
https://sourceforge.net/projects/fsmark/
```
tar zxvf fs_mark-3.3.tgz
cd fs_mark
make
# fail:
# sudo dnf install glibc-static
# sudo zypper install glibc-devel-static
fs_mark -d /tmp -n 2500 -s 10240
iostat -x -d /dev/sda 2 10
```

## I/O Scheduler

- `cat /sys/block/sda/queue/scheduler`
- `echo bfq > /sys/block/sda/queue/scheduler`
- `cat /sys/block/sda/queue/sheduler`
- `ls /sys/block/sda/queue/iosched/`
- `.../rotational`
```
sudo ./lab_iosched.sh 100 10
```

## FS and VFS

- https://sourceforge.net/projects/ntfs-3g/
- `ln`, `ls -liF`
- `cat /proc/filesystems`
```
lsmod
dd if=/dev/zero of=junk bs=1M count=512
sudo /sbin/mkfs.xfs junk
sudo mount junk /mnt
df -h
lsmod
```
```
sudo mkdir /mnt/tmpfs
sudo mount -t tmpfs none /mnt/tmpfs
df -h /mnt/tmpfs
sudo mount -t tmpfs -o size=1G none /mnt/tmpfs
sudo umount /mnt/tmpfs
df -h /dev/shm
df -h | grep 'tmpfs'
```

## Disk partitioning

- https://www.hp.com/us-en/shop/tech-takes/sas-vs-sata
- `sudo fdisk -l /dev/sda | grep -i sector`
- `ls -l`, `sudo mkfs.ext4 /dev/sdxy`
- `sudo blkid /dev/sdx*`
- `lsblk`
- `dd if=/dev/sda of=mbrbackup bs=512 count=1`, `sudo dd if=mbrbackup of=/dev/sdx bs=512 count=1`, `sudo sgdisk -p /dev/sda`
- `fdisk`, `sfdisk`, `parted`, `gparted`, `gdisk`, `sgdisk`
- `sudo partprobe -s`, `cat /proc/partitions`
- `mkfs.ext4 /dev/sdxy`
```
dd if=/dev/zero of=imagefile bs=1M count=1024
mkfs.ext4 imagefile
mkdir mntpoint
sudo mount -o loop imagefile mntpoint
sudo umount mntpoint
sudo losetup /dev/loop2 imagefile
sudo mount /dev/loop2 mntpoint
sudo umount mntpoint
sudo losetup -d /dev/loop2
```
```
sudo fdisk -C 130 imagefile
	m
	n
	+256M
	n
	+256M
	w
```
```
sudo losetup -f
sudo losetup /dev/loop1 imagefile
losetup -a
sudo parted -s /dev/loop1 mklabel msdos
sudo parted -s /dev/loop1 unit MB mkpart primary ext4 0 256
sudo parted -s /dev/loop1 unit MB mkpart primary ext4 256 512
sudo parted -s /dev/loop1 unit MB mkpart primary ext4 512 1024
fdisk -l /dev/loop1
ls -l /dev/loop1*
sudo mkfs.ext3 /dev/loop1p1
sudo mkfs.ext4 /dev/loop1p2
sudo mkfs.ext4 /dev/loop1p3
mkdir mnt1 mnt2 mnt3
sudo mount /dev/loop1p1 mnt1
sudo mount /dev/loop1p2 mnt2
sudo mount /dev/loop1p3 mnt3
df -Th
sudo umount mnt1 mnt2 mnt3
rmdir mnt1 mnt2 mnt3
sudo losetup -d /dev/loop1
```

## Filesystem features: attributes, creating, checking, mounting

- `lsattr`, `chattr`, `man chattr`
- `sudo mkfs -t ext4 /dev/sdxy`, `sudo mkfs.ext4 /dev/sd`
- `sudo touch /forcefsck`
- `mount -t ext /dev/sdxy /home`
- `sudo mount LABEL=`, `-L`, `UUID`, `-U`
- `sudo mount -o remount,ro /myfs` +
- `umount /dev/sdx`, `fuser`, `lsof`
- `sudo mount -t nfs myserver.com:/shdir /mnt/shdir​`
- `/etc/fstab`, `LABEL=Sam128 /SAM ext4 noauto,x-systemd.automount,x-systemd.device-timeout=10,x-systemd.idle-timeout=30 0 0`, `sudo systemctl daemon-reload`, `sudo systemctl restart local-fs.target`
- `df -h -T`
```
touch /tmp/appendit
cat /etc/hosts > /tmp/appendit
diff /etc/hosts /tmp/appendit
sudo chattr +a /tmp/appendit
lsattr

```
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
- `tar cvf file.tar dir1`, `tar -cvf file.tar dir1`
- `tar --extract --same-permissions --verbose --file /dev/st0`
- `tar -xpvf /dev/st0`, `tar xpvf /dev/st0`
- `tar xvf /dev/st0 somefiletorestore`
- `tar --list --file /dev/st0`, `tar -tf /dev/st0`
- `tar --create --newer '2011-12-1' -vzf backup1.tgz /var/tmp`, `tar --create --after-date '2011-12-1' -vzf backup1.tgz /var/tmp`
- https://www.kernel.org/
- `tar zcvf source.tar.gz source`, `tar jcvf source.tar.bz2 source`, `tar Jcvf source.tar.xz source`
- `tar cvf source.tar source ; gzip -v source.tar`
- `tar xzvf source.tar.gz`, `tar xjvf source.tar.bz2`, `tar xJvf source.tar.xz`
- `tar xvf source.tar.gz`
- `dd if=input-file of=output-file options`
- `dd if=/dev/zero of=outfile bs=1M count=10`, `dd if=/dev/sda of=/dev/sdb`, `dd if=/dev/sda of=sdadisk.img`, `dd if=/dev/sda1 of=partition1.img`, `dd if=/dev/cdrom of=tgsservice.iso bs=2048`
- `rsync [options] sourcefile destinationfile`
- `rsync file.tar someone@backup.mydomain:/usr/local`, `rsync -r --dry-run /usr/local /BACKUP/usr`
- `rsync -r project-X archive-machine:archives/project-X`
- `ls | cpio --create -O /dev/st0`, `cpio -i somefile -I /dev/st0`, `cpio -t -I /dev/st0`
- http://www.amanda.org/
- https://www.bacula.org/7.0.x-manuals/en/main/Main_Reference.html
- https://clonezilla.org/
- `mkdir /tmp/backup`, `cd /usr ; tar zcvf /tmp/backup/include.tar.gz include`, `cd /usr ; tar jcvf /tmp/backup/include.tar.bz2 include`, `cd /usr ; tar Jcvf /tmp/backup/include.tar.xz include`, `tar -C /usr -zcf include.tar.gz include`, `tar -C /usr -jcf include.tar.bz2 include`, `tar -C /usr -Jcf include.tar.xz include`, `du -sh /usr/include`, `ls -lh include.tar.*`, `tar tvf include.tar.xz`, `cd .. ; mkdir restore ; cd restore`, `tar xvf ../backup/include.tar.bz2`, `diff -qr include /usr/include`
- `(cd /usr ; find include | cpio -c -o > /home/student/backup/include.cpio)`, `(cd /usr ; find include | cpio -c -o | gzip -c > /home/student/backup/include.cpio.gz)`, `ls -lh include*`, `cpio -ivt < include.cpio`, `cd ../restore`, `cat ../backup/include.cpio | cpio -ivt`, `gunzip -c include.cpio.gz | cpio -ivt`, `rm -rf include`, `cpio -id < ../backup/include.cpio`, `ls -lR include`, `cpio -idv < ../backup/include.cpio`, `diff -qr include /usr/include`
- `rm -rf include`, `rsync -av /usr/include .`, `rsync -av /usr/include .`, `rsync -av /usr/include include`, `rsync -av --delete /usr/include .`, `rm -rf include/xen`, `rsync -av --delete --dry-run /usr/include .`, `rsync -av --delete  /usr/include .`
- `#!/bin/sh`, `set -x`, `rsync --progress -avrxH --delete $*`

## Linux security modules

- https://selinuxproject.org/page/Main_Page
- https://gitlab.com/apparmor
- http://schaufler-ca.com/
- https://tomoyo.osdn.jp/
- https://www.starlab.io/blog/a-brief-tour-of-linux-security-modules
- https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/index
- `sudo apt install policycoreutils selinux-utils selinux-basics`
- `sestatus`
- CentOS, Suse: `/etc/sysconfig/selinux`, Ubuntu: `/etc/selinux/config`
- `sudo selinux-activate`
- `getenforce`, `sudo setenforce Permissive`, `Enforcing`, `Disabled`
- `/etc/selinux/config`, `SELINUX=disabled`, `selinux=0`
- `etc/selinux/[SELINUXTYPE]`, `targeted`, `minimum`, `MLS`
- `ls -Z`, `ps auZ`
- `chcon -t etc_t somefile`, `chcon --reference somefile someotherfile`, `ls -Z`
- `cd /tmp/`, `touch tmpfile`, `ls -Z tmpfile`, `cd`, `touch homefile`, `ls -Z homefile`, `mv /tmp/tmpfile .`, `ls -Z`
- `ls -Z`, `restorecon -Rv /home/user`, `ls -Z`
- `policycoreutils-python`, `semanage fcontext`
- `mkdir /virtualHosts`, `ls -Z`, `semanage fcontext -a -t httpd_sys_content_t /virtualHosts`, `ls -Z`, `restorecon -RFv /virtualHosts`, `ls -Z`
- `getsebool`, `setsebool`, `semanage boolean -l`
- `setsebool allow_ftpd_anon_write on`, `getsebool allow_ftpd_anon_write`
- `echo 'File created at /root' > rootfile`, `mv rootfile /var/www/html/`, `wget -O - localhost/rootfile`, `tail /var/log/messages`
- `sudo systemctl [start|stop|restart|status] apparmor`, `sudo systemctl [enable|disable] apparmor`, `sudo apparmor_status`, `ps aux | grep libvirtd`
- `aa-enforce`, `aa-complain`, `/etc/apparmor.d`, apparmor-profiles: `ls /etc/apparmor.d`
- `man apparmor.d`
- `rpm -qil apparmor-utils | grep bin`, `ls -l /usr/sbin/*complain`
- `apparmor_status`, `apparmor_notify`, `complain`, `enforce`, `disable`, `logprof`, `easyprof`
- `sudo dnf install  httpd`, `elinks http:/localhost`, `sudo sh -c "echo file1 > /var/www/html/file1.html"`, `elinks -dump http://localhost/file1.html`, `sudo cd /root`, `sudo sh -c "echo file2 > file2.html"`, `sudo mv file2.html /var/www/html`, `elinks -dump http://localhost/file2.html`, `cd  /var/www/html`, `ls -Z file*html`, `sudo chcon -t httpd_sys_content_t file2.html`, `elinks http://localhost/file2.html`
- `sudo apt-get install apparm*`, `sudo cp /bin/ping /bin/ping-x`, `sudo ls -l /bin/ping-x`, `sudo getcap /bin/ping-x`, `ping-x -c3 -4 127.0.0.1`, `sudo setcap cap_net_raw+ep  /bin/ping-x`, `ping-x  -c3 -4 127.0.0.1`, `sudo aa-status`, `sudo aa-status | grep -e "ˆ[[:alnum:]]" -e ping`, `sudo aa-genprof /bin/ping-x`, `ping-x  -c3 -4 127.0.0.1`, `AASF`, `sudo cat /etc/apparmor.d/bin.ping-x`, `ping-x -c3 -4 127.0.0.1`, `ping-x -c3  -6 ::1`

## Local system security

- https://help.ubuntu.com/community/Grub2/Passwords
- `/etc/fstab`, `nodev`, `nosuid`, `noexec`, `ro`
- `mount -o ro,noexec,nodev /dev/sda2 /edsel`
- `/dev/sda2 /edsel  ext4 ro,noexec,nodev 0 0`
- `chmod u+s somefile`, `chmod g+s somefile`, `chmod g+s somedir`
- `setuid`, `setgid`
- `dd if=/dev/zero of=image bs=1M count=100`, `sudo mkfs.ext3 image`, `mkdir mountpoint`, `sudo mount -o loop image mountpoint`, `sudo cp /bin/ls mountpoint`, `mountpoint/ls`, `sudo umount mountpoint ; sudo mount -o noexec,loop image mountpoint` or `sudo mount -o noexec,remount image mountpoint`, `mountpoint/ls`, `sudo umount mountpoint`, `rm image`, `rmdir mountpoint`
- `/home/student/image  /home/student/mountpoint    ext3    loop,rw,noexec 0 0`

## Basic troubleshooting

- `/var/log/messages`, `/var/log/secure`
- `ifconfig`, `ip`
- `lsmod`, `/proc`, `/sys`, `/proc/interrupts`, `/sys/class/net`
- `ping`, `traceroute`, `mtr`
- `route -n`
- `dig`, `host`
- `rpm -V some_package`, `rpm -Va`, `debsums options some_package`, `aide --check`
- `/etc/fstab`
- `sudo mount -o remount,rw /`, `sudo mount -a`
- `Ctrl-Alt-FX`

## System rescue

- `fdisk`, `mdadm`, `pvcreate`, `vgcreate`, `lvcreate`, `mkfs`
- `ifconfig`, `route`, `traceroute`, `mtr`, `host`, `ftp`, `scp`, `ssh`
- `bash`, `chroot`, `ps`, `kill`, `vi`, `dd`, `tar`, `cpio`, `gzip`, `rpm`, `mkdir`, `ls`, `cp`, `mv`, `rm`
- `/mnt/sysimage`, `sudo chroot /mnt/sysimage`, `/mnt/source`
- `sudo rpm -ivh --force --root=/mnt/sysimage /mnt/source/Packages/vsftpd-2*.rpm`
- `dd if=boot.iso of=/dev/sdX`
- `livecd-tools`, `liveusb-creator`
- `e`, `emergency`, `single`
- `dd if=/dev/sda of=/root/mbrsave bs=446 count=1`, `sudo ls -l /root/mbrsave`, `dd if=/dev/zero of=/dev/sda bs=446 count=1`, `dd if=/mnt/sysimage/root/mbrsave of=/dev/sda bs=446 count=1`
- `mount /dev/cdrom /mnt/source`, `mount /dev/sdXY /mnt/mysys`, `rpm -ivh --force --root /mnt/mysys /mnt/source/Packages/zsh*.rpm`

<!------ L2 ------>

# L2

## Linux networking: concept and review

- `
- `
- `

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
