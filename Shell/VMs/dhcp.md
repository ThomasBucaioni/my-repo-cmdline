# DHCP config

## File `/etc/dhcp/dhcpd.conf`

```
option domain-name "mydomtest.xyz";
option domain-search "mydomtest.xyz";

option domain-name-servers 10.0.9.1;

default-lease-time 600;
max-lease-time 7200;
authoritative;

subnet 10.0.9.0 netmask 255.255.255.0 {
	# default gateway
	option routers		10.0.9.1;
	option subnet-mask	255.255.255.0;

	range dynamic-bootp 10.0.9.50 10.0.9.59;

	host rhel-server-unattended {
		hardware ethernet 	52:54:00:8f:7a:85;
		fixed-address		10.0.9.21;
	}	
}
```

## Hints

```
dhclient
ip link enp8s0 down ; ip link enp8s0 up
nmcli con modify ethernet-enp7s0 +ipv4.dns 10.0.9.1
```

