#!/bin/bash
# under Debian like: https://opensource.com/article/21/4/securing-linux-servers

# 1. Run updates
sudo apt-get update && apt-get upgrade

# 2. Enable firewall protection
sudo apt-get install ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
#ufw allow <service>
ufw allow ssh
sudo ufw enable

# 3. Strengthen password protection
sudo apt-get install libpam-cracklib
vi /etc/pam.d/common-password
# To enforce password length: minlen=12
# To prevent password reuse: remember=5
# To enforce password age:
vi /etc/login.defs
# PASS_MIN_AGE: 3
# PASS_MAX_AGE: 90
# PASS_WARN_AGE: 14

# To enforce character specifications:
vi /etc/pam.d/common-password
# pam_cracklib.so (...) lcredit=-1 ucredit=-1 dcredit=-1 ocredit=-1

# 4. Disable nonessential services that are prone to exploitation
sudo apt-get install systemd
systemctl list-units
#systemctl stop <service>
#systemctl disable <service>
#systemctl status <service>

# 5. Check for listening ports
netstat -tulpn

# 6. Scan for malware
sudo apt-get install clamav
sudo freshclam
sudo clamscan -r --bell -i /

# systemd timers: https://opensource.com/article/20/7/systemd-timers
systemctl status *timer
# cron: https://opensource.com/article/21/2/linux-automation
which anacron
mkdir -p ~/.local/etc/cron.daily ~/.var/spool/anacron
cp example ~/.local/etc/cron.daily
