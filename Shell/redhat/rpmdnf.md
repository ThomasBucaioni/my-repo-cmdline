# RPM and DNF management

## Configuring repositories

### Global repository:
```
vim /etc/dnf/dnf.conf
gpgcheck=1
installonly_limit=3
```

### EPEL repository:
```
vim /etc/yum.repos.d/epel.repo
[epel]
name=Extra Packages for Enterprise Linux 8 - $basearch
#baseurl=https://download.example/pub/epel/8/Everything/$basearch
metalink=https://mirrors.fedoraproject.org/metalink?repo=epel-8&arch=$basearch&infra=$infra&content=$contentdir
enabled=0
gpgcheck=0
countme=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-8
```

### Enable and disable repositories

```
dnf repolist --all
dnf config-manager --set-enabled epel
dnf config-manager --set-disabled epel-testing
dnf repolist --all
```


