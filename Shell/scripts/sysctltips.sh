#!/bin/bash
# https://opensource.com/article/21/4/sysadmins-love-systemd
journalctl --list-boots
journalctl --pager-end
journalctl --pager-end --catalog
journalctl --pager-end --catalog --boot 42
journalctl --pager-end --catalog --boot 42 --unit sshd
systemctl cat sshd
# [Unit]
# Description=OpenSSH server daemon
# Documentation=man:sshd(8) man:sshd_config(5)
# After=network.target sshd-keygen.target
# Wants=sshd-keygen.target

# [Service]
# Type=notify
# EnvironmentFile=-/etc/crypto-policies/back-ends/opensshserver.config
# EnvironmentFile=-/etc/sysconfig/sshd
# ExecStart=/usr/sbin/sshd -D $OPTIONS $CRYPTO_POLICY
# ExecReload=/bin/kill -HUP $MAINPID
# KillMode=process
# Restart=on-failure
# RestartSec=42s

# [Install]
# WantedBy=multi-user.target
systemctl edit sshd
systemctl is-active sshd
systemctl is-active foo
systemctl stop sshd
systemctl start sshd
systemctl enable sshd
systemctl enable sshd --now
