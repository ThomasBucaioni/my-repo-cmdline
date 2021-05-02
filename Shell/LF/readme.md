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

-`