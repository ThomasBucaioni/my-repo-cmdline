# Packages with DNF

## Search for available packages

```
sudo dnf search virtualization API
sudo dnf search web server reverse proxy
sudo dnf search traceroute ping
```

## Provides specific utilities

```
dnf provides nmap
dnf list nmap
dnf info nmap
dnf repoquery --available -l nmap
dnf provides netstat
dnf list net-tools
dnf info net-tools
dnf repoquery --installed -l net-tools
```

## Provides specific files

```
dnf provides "*/smb.conf"
dnf list samba-common
dnf repoquery --installed -i samba-common
dnf repoquery --installed -f "/etc/chrony.conf"
dnf repoquery --installed -f "/etc/chrony.conf" -i
```

## Managing packages

```
dnf install sysstat nmap mtr
dnf list sysstat nmap mtr
dnf repoquery -i vsftpd
dnf install vsftpd-3.0.3-33.e18
dnf remove drbd htop
dnf autoremove
```

### Package groups

```
dnf group remove "system tools"
dnf group list
```

### Modules

```
dnf module list nginx
dnf module remove nginx
dnf module list nginx
dnf module list postgresql
dnf module enable postgresql:13
dnf module list postgresql
dnf module install postgresql
dnf module list postgresql
```

### Update

```
dnf clean all
dnf check-upgrade
dnf upgrade
dnf check-update
```

## Managing packages with RPM

### Remove packages

```
rpm -evh nmap telnet
rpm -evh mysql
rph -evh maridb-connector-c-config
rpm -evh mysql-common
rph -evh mariadb-connector-c-config
```

### Install and upgrade

```
rpm -ivh htop-3.2.1-1.el8.x86_64.rpm mtr-0.92-3.el8.x86_64.rpm
rpm -Uvh wget-1.19.5-10.el8.x86_64.rpm
rpm -Uvh nginx/*
```

## Investigating

### Query installed

```
rpm -qa
rpm -qf usr/bin/iostat
rpm -qi sysstat
rpm -qc sysstat
rpm -q --changelog sysstat
rpm -qf /var/lib/dav
rpm -q httpd
rpm -qd httpd
rpm -q --scripts httpd
```

### Query uninstalled

```
rpm -qip nginx
rpm -qRp nginx
rpm -qcp nginx
rpm -qp --changelog nginx
rpm -qip vsftpd
rpm -qpl vsftpd
rpm -qpd vsftpd
rpm -qp --scripts vsftpd
```

### Verify

```
rpm -V nmap mtr
rpm -V --nogroup sysstat
rpm -V --nodeps --nordev httpd
```


