# Troubleshooting

## CPU

```
pminfo | grep cpu
pmrep -a /var/log/pcp/pmlogger/app/20220202.13.30.0 -S "@Feb 2 00:00:00 2022" -T "@Feb 3 00:00:00 2022" -t 10s kernel.cpu.util.sys | less
pcp atop
pmrep kernel.cpu.util.sys -T 1m
ps axjf | less
systemctl list-units --type=service --state=running
```

## FS

```
dumpfs /dev/disk
e2fck -p /dev/disk -b block_number
xfs_repair /dev/disk
```

## LVM

```
vgcfgrestore -l vgdata
vgcfgrestore -f /backup vgdata
lvchange -an /dev/vgdata/lvdata
lvchange -ay /dev/vgdata/lvdata
```

## Crypted FS

```
cat /etc/crypttab
cryptsetup luksOpen /dev/mapper/vgdata-lvdata luks-vgdata-lvdata --key-file /root/secret.key
cryptsetup luksHeaderRestore /dev/mapper/vgdata-lvdata --header-backup-file /root/backups/vgdata-lvdata.header
cryptsetup luksOpen /dev/mapper/vgdata-lvdata luks-vgdata-lvdata --key-file /root/secret.key
```

### Encryption eCryptfs

```
sudo mount -t ecryptfs /opt/protected /opt/protected
sudo cp /etc/profile.d/* /opt/protected/
cat /opt/protected/apps-bin-path.sh
sudo umount /opt/protected
cat /opt/protected/apps-bin-path.sh
```

## ISCSI

```
systemctl status target
ss -lpt # iscsi-target
telnet 10.0.1.101 3260
targetcli # ls
cat /etc/iscsi/initiatorname.iscsi
iscsiadm -m discovery -t sendtargets -p 10.0.1.101
iscsiadm -m node -T iqn.2003-01.org.linux-iscsi.ip-10-0-1-10.x8664:sn.a3776832068c -l
get auth
vim /etc/iscsi/iscsid.conf # /CHAP
systemctl restart iscsi
iscsiadm -m node
iscsiadm -m session
iscsiadm -m node -T iqn.2003-01.org.linux-iscsi.ip-10-0-1-10.x8664:sn.a3776832068c -l
iscsiadm -m node -o delete
iscsiadm -m discovery -t sendtargets -p 10.0.1.101
iscsiadm -m node -T iqn.2003-01.org.linux-iscsi.ip-10-0-1-10.x8664:sn.a3776832068c -l
iscsiadm -m session
```

## Package versioning

```
dnf update ruby
dnf list --showduplicates ruby
dnf versionlock list
dnf versionlock delete ruby
dnf versionlock list
dnf update ruby
ruby -v
```

## RPM database

```
cd /var/lib/rpm
ls
/usr/lib/rpm/rpmdb_verify Packages
lsof | grep /var/lib/rpm
rm -rf /var/lib/rpm/__db*
mv Packages Packages.bak
/usr/lib/rpm/rpmdb_dump Packages.bak | /usr/lib/rpm/rpmdb_load Packages
/usr/lib/rpm/rpmdb_verify Packages
rpm -vv --rebuilddb
echo "8" >> /etc/yum/vars/releasever
dnf clean all
dnf repolist -v
```


