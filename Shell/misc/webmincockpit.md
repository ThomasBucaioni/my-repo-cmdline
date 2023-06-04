# Webmin and Cockpit monitoring

## Install Webmin

### Repo

```
vim /etc/yum.repos.d/webmin.repo

[Webmin]
name=Webmin Distribution Neutral
baseurl=http://download.webmin.com/download/yum
enabled=1
gpgcheck=1
gpgkey=http://www.webmin.com/jcameron-key.asc"

yum -y install webmin
```

### Make a service

```
vim /etc/systemd/system/webmin.service

Unit]
Description=Webmin
Requires=local-fs.target
After=basic.target
Conflicts=shutdown.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/etc/webmin/start
ExecStop=/etc/webmin/stop
ExecReload=/etc/webmin/reload

[Install]
WantedBy=multi-user.target

systemctl daemon-reload
sudo systemctl enable --now webmin
systemctl status webmin
```

### Config

```
vim /etc/webmin/miniserv.conf

port=8080
listen=8080

sudo systemctl restart webmin
```

## Cockpit

### Install

```
yum install cockpit
systemctl enable --now cockpit
systemctl status cockpit
systemctl status cockpit.socket
```

### Add modules

```
yum list cockpit*
yum install cockpit-dashboard cockpit-doc cockpit-packagekit cockpit-storaged

https://IP:9090/
```
