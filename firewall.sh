#!/bin/sh
#
# firewall.sh

# WAN and LAN interfaces
IFACE_LAN=enp2s0
IFACE_WAN=enp0s29f7u7
IFACE_LAN_IP=172.168.1.0/24

# Accept all
iptables -t filter -P INPUT ACCEPT
iptables -t filter -P FORWARD ACCEPT
iptables -t filter -P OUTPUT ACCEPT
iptables -t nat -P INPUT ACCEPT
iptables -t nat -P PREROUTING ACCEPT
iptables -t nat -P POSTROUTING ACCEPT
iptables -t nat -P OUTPUT ACCEPT
iptables -t mangle -P INPUT ACCEPT
iptables -t mangle -P PREROUTING ACCEPT
iptables -t mangle -P FORWARD ACCEPT
iptables -t mangle -P POSTROUTING ACCEPT
iptables -t mangle -P OUTPUT ACCEPT

# Reset the counters
iptables -t filter -Z
iptables -t nat -Z
iptables -t mangle -Z

# Delete all active rules and personalized chains
iptables -t filter -F
iptables -t filter -X
iptables -t nat -F
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X

# Default policy
iptables -P INPUT DROP
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT

# Trust ourselves
iptables -A INPUT -i lo -j ACCEPT

# Ping
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
iptables -A INPUT -p icmp --icmp-type time-exceeded -j ACCEPT
iptables -A INPUT -p icmp --icmp-type destination-unreachable -j ACCEPT

# Established connections
iptables -A INPUT -m state --state ESTABLISHED -j ACCEPT

# SSH
iptables -A INPUT -p tcp -i $IFACE_LAN --dport 22 -j ACCEPT
# iptables -A INPUT -p tcp -i $IFACE_WAN --dport 22 -j ACCEPT # too many NATs to cross

# Dnsmasq
iptables -A INPUT -p tcp -i $IFACE_LAN --dport 53 -j ACCEPT
iptables -A INPUT -p udp -i $IFACE_LAN --dport 53 -j ACCEPT
iptables -A INPUT -p udp -i $IFACE_LAN --dport 67:68 -j ACCEPT

# TCP
iptables -A INPUT -p tcp -i $IFACE_LAN --dport 80 -j ACCEPT
iptables -A INPUT -p tcp -i $IFACE_WAN --dport 80 -j ACCEPT

# Packet forwarding activation
iptables -t nat -A POSTROUTING -o $IFACE_WAN -s $IFACE_LAN_IP -j MASQUERADE
sysctl -q -w net.ipv4.ip_forward=1

# Log refused packets
iptables -A INPUT -m limit --limit 2/min -j LOG --log-prefix "IPv4 packet rejected ++ "
iptables -A INPUT -j DROP

# Save the configuration
service iptables save
