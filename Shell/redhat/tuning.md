# System Tuning

## Kernel behavior

### Kernel parameters

```
cat /proc/cmdline
dmesg | grep "Command line"
sysctl -a
sysctl -a | wc -l
sysctl -a | grep ipv4.ip
sysctl net.ipv4.ip_forward_update_priority
sysctl -n net.ipv4.ip_forward_update_priority
cat /proc/sys/net/ipv4/ip_forward_update_priority
sysctl fs.quota.drops
cat /proc/sys/fs/quota/drops
```

### Modify kernel parameters

```
sysctl net.ipv4.ip_forward
sysctl net.ipv4.ip_forward=0
sysctl net.ipv4.ip_forward
cat /etc/sysctl.conf
vim /etc/sysctl.d/10-network.conf
net.ipv6.conf.default.forwarding=1
sysctl -p /etc/sysctl.d/10-network.conf
echo "net.ipv6.conf.default.forwarding=1" >> /etc/sysctl.d/10-network.conf
```

### Optimizing

```
lsmod
lsmod | sort
lsmod | grep bluetooth
lsmod | grep bridge
modinfo bluetooth
modprobe bluetooth
modprobe -r bluetooth
echo bluetooth > /etc/modules-load.d/bluetooth.conf
rm /etc/modules-load.d/bluetooth.conf
vim /etc/modprobe.d/blacklist.conf
  blacklist bluetooth
  install bluetooth /bin/false
cp /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r).bak.$(date +%m-%d-%H%M%S).img
dracut -f -v
```

## Analyzing performances

### Common utilities

```
ps aux --sort vsize
ps -ef --forest
ps aux | grep -v grep | grep -e VSZ -e bash
ps -eo user,pid,%cpu,%mem,cmd | grep -v grep | grep -e %CPU -e bash
watch -n 5 "ps -eo user,pid,%cpu,%mem,cmd | grep -v grep | grep -e %CPU -e bash"
top # P N R x b f k d o (%CPU>0 COMMAND=sshd) O c U u V W ~/.toprc
top -p $pid
top -p $pid -b -n 5 > topdata.txt
htop
nmon # nmonchart nmonvisualizer
nmon -f -s 5 -c 2 -m /home/user/
glances # h
glances -w -p 8080
glances --export influxdb
```

### Specialized tools: `mpstat`, `iostat`, `vmstat`

```
dnf install -y sysstat
mpstat
mpstat 3 5
mpstat -I ALL
cat /proc/interrupts
cat /proc/softirqs
iostat
iostat -x
iostat -d 3 5
vmstat
vmstat -t
vmstat -t 3 5
vmstat -d
vmstat -s
```

### Specialized tools: `pidstat`, `sar`, `sadf`

```
pidstat -p ALL
pidstat -p $pid
pidstat -C "sshd"
pidstat -p $pid -r 2 5
pidstat -t -C "sshd" -l
pidstat -ruUdhl -C "bash"
sar
sar -u 2 5
sar -r 2 5
sar -F 2 5
sar -B
sadf
sadf /var/log/sa/saXY
sadf /var/log/sa/saXY -- -r
sadf /var/log/sa/saXY -- -A -B -d -H ...
sadf -d -g -j -r -x
sadf /var/log/sa/saXY -g -s 10:00 -e 17:00 -- -B > pagingreport_svgformat.svg
sadf -dh /var/log/sa/saXY -- -B | sed 's/;/,/g' > csv_paging_report.csv # database format converted
```

### Valgrind

```
yum group install "Development Tools"
valgrind --version
valgrind --tool=memcheck --leak-check=yes --show-reachable=yes --num-callers=20 --track-fds=yes ./memleak
valgrind --tool=memcheck --leak-check=yes --show-reachable=yes --num-callers=20 --track-fds=yes ./memerror
valgrind --tool=cachegrind --log-file=cachetest.out ./cachetest
cg_annotate cachegrind.out.*
valgrind --tool=helgrind -s ./hgrindtest
valgrind --tool=drd --read-var-info=yes ./rwlock_race
valgrind --tool=massif --time-unit=B ./massiftest
ms_print massif.out.*
valgrind --tool=callgrind --dump-instr=yes --simulate-cache=yes --collect-jumps=yes ./threads
callgrind_annotate callgrind.out.*
```

### SystemTap

```
yum group install "Development Tools"
# yum install systemtap systemtap-runtime
yum install coreutils
stap-prep
name -r
yum install kernel-debuginfo kernel-debuginfo-common kernel-devel-KERNELVER
stap -v -e 'probe vfs.read {printf("read performed\n"); exit()}'
stap -e 'probe kernel.function("do_sys_open") {log("hello world") exit()}'
stap disktop.stp
stap eventcount.stp 'syscall.read'
stap nettop.stp
stap tcp_connections.stp
stap procmod_watcher.stp 
stap -g ttyspy.stp
stap watchdog.stp 'syscall.nanosleep' 'syscall.nanosleep.return' 1000
```

### eBPF

```
yum install bcc-tools
cd /usr/share/bcc/tools
./execsnoop
./execsnoop -TU
./execsnoop -TU -n ls
./opensnoop
./opensnoop -U
./opensnoop -U -u UID
./ttysnoop DEVICE#
./tcplife
./tcplife -L 8000
./tcplife -p PID
./tcplife -sT
./killsnoop
./gethostlatency
./biotop
./biotop -C
./biotop -C 5 10
```

### Co-Pilot

#### Install

```
# Server
yum install pcp pcp-zeroconf
systemctl status pmcd
systemctl status pmlogger
systemctl status pmie
yum install cockpit-pcp
pmlogconf -r /var/lib/pcp/config/pmlogger/config.default

yum install pcp-system-tools
echo "myIP n n myDir/pmlogger/myHostname -r -T24h10m -c config.remote" >> /etc/pcp/pmlogger/control.d/remote
systemctl restart pmcd pmlogger
ss -tlp | grep 44321

# Client
yum install pcp-system-tools
echo "-i myIP" | sudo tee -a /etc/pcp/pmcd/pmcd.options
setsebool -P pcp_bind_all_unreserved_ports on
systemctl enable --now pmcd pmlogger
ss -tlp | grep 44321
```

####  Metrics and performances

```
pcp

iostat -x
pcp iostat
pmchart -c Iostat

vmstat
pcp vmstat

mpstat
pcp mpstat

top
pcp atop

pmdumptext -Xlimu -t 2sec 'kernel.all.load[1]' mem.util.used disk.partitions.write -h localhost

pminfo --fetch containers.name containers.state.running

pmprobe -I network.interface.up

pmprobe -I --container CONTAINERNAME network.interface.up

ls /var/log/pcp/pmlogger/HOSTNAME

pmdumplog -L /var/log/pcp/pmlogger/HOSTNAME/LOGNAME

pmlogextract *.0 ../hostarchive

pmchart -z -a hostarchive -t 10m -O-0 -s 400 -v 400 -geometry 800x450 -c CPU -c Loadavg

pmrep -z -a hostarchive -t 10m -p -S'@19:45' -s 20 kernel.all.load kernel.all.cpu.{user,sys,wait.total} disk.all.total_bytes
```


