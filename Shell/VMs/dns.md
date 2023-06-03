# DNS config

## Named

File `/etc/named.conf'

```
options {
	listen-on port 53 { 127.0.0.1; 10.0.9.1; };
//	listen-on-v6 port 53 { ::1; };
//	forwarders { 10.0.9.1; 1.1.1.1; };
  ...
  allow-query     { localhost; 10.0.9.0/24; };
  ...
}

...

zone "mydomtest.xyz" IN {
	type master;
	file "mydomtest.xyz.zone";
};

zone "9.0.10.in-addr.arpa" IN {
	type master;
	file "mydomtest.xyz.rev";
};

## Zone file `/var/named/mydomtest.xyz.zone`

```
; Authoritative data for mydomtest.xyz zone
;
$TTL 1D
@ IN SOA rhel-server.mydomtest.xyz root.rhel-server.mydomtest.xyz. (
	2023060301 	; serial
	1D		; refresh
	1H		; retry
	1W		; expire
	3H )		; minimum

$ORIGIN	mydomtest.xyz.
mydomtest.xyz.	IN	NS	rhel-server.mydomtest.xyz.
rhel-server	IN	A	10.0.9.1
server		IN	CNAME	rhel-server
router		IN	CNAME	rhel-server
rhel-server-unattended	IN	A	10.0.9.21
workstation1	IN	CNAME	rhel-server-unattended
ws1		IN	CNAME	rhel-server-unattended
rhel-server-unattended2	IN	A	10.0.9.22
rhel-server-unattended3	IN	A	10.0.9.23
```

## Reverse zone file `/var/named/mydomtest.xyz.rev`

```
; reverse mapping for mydomtest.xyz zone
;
$TTL 1D
@	IN	SOA	rhel-server.mydomtest.xyz.	root.rhel-server.mydomtest.xyz. (
	2023060301	; serial
	1D		; refresh
	1H		; retry
	1W		; expire
	3H )		; minimum

@	IN	NS	rhel-server.mydomtest.xyz.
1	IN	PTR	router.mydomtest.xyz.
1	IN	PTR	rhel-server.mydomtest.xyz.
21	IN	PTR	rhel-server-unattended.mydomtest.xyz.
```

