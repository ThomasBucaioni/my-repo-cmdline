# Build VMs

## Qemu

### Make and manage a Qcow image

```
qemu-img create -f qcow2 ubuntu.qcow2 10G
qemu-img resize ubuntu.qcow2 +1G
qemu-img info ubuntu.qcow2
qemu-img snapshot -c ubuntu_snapshot_yyyy_mm_dd ubuntu.qcow2
qemu-img snapshot -l ubuntu.qcow2
qemu-img snapshot -a 1 ubuntu.qcow2
qemu-img snapshot -d ubuntu_snapshot_yyyy_mm_dd
```

### Install an OS on the Qcow image

Install an iso on the image:
```
qemu-system-x86_64 \
-m 4096\
-hda ~/myVms/ubuntu.qcow2  \
-cdrom ~/iso/Ubuntu20.04.iso \
```

## KVM

### Virt-install

Build an Rhel9.2 instance:
```
wget https://url/to/distrib.iso
mount -o ro distrib.iso /mnt
virt-install \
--name myguestname \
--memory 4096 \
--disk path=/var/lib/libvirt/images/mydiskimage.img,size=20 \
--cdrom distrib.iso \
--nographics \
--os-type linux \
--network network:mybridge \
--boot kernel=casper/vmlinuz,initrd=casper/initrd,kernel_args="console=ttyS0"

mount -o ro,loop -t iso9660 /path/to/image.iso /mnt/rhel-install
cp -r /mnt/rhel-install /var/www/html/
systemctl start httpd
curl -I http://mylocalip/rhel-install
virt-install --name rhel-server-unattended \
  --location http://10.0.0.1/rhel-install/ \
  --os-variant rhel9.2 --memory 4096 --vcpus 4 --disk size=20 \
  --nographics \
  --extra-args="inst.ks=file:/centos7-ks.cfg console=ttyS0,115200n8" \
  --network network:internetbridge \
  --initrd-inject centos7-ks.cfg \
  --disk /var/lib/libvirt/images/rhel-server-unattended.qcow2
```

### Virsh

Manage VMs:
```
virsh console server
virsh destroy server
virsh start server --console
virsh undefine server
virsh edit server
virsh list --all
```

#### Networking

Define an internal and external switch
```
<network>
  <name>external</name>
  <bridge name="extbridge"/>
  <forward mode="nat"  dev='enpXsYonhost'/>
  <ip address="10.10.10.1" netmask="255.255.255.0">
	  <dhcp>
      <range start="10.10.10.2" end="10.10.10.254"/>
    </dhcp>
  </ip>
</network>

<network>
  <name>internal</name>
  <bridge name="intbridge"/>
</network>
```

Activate the switches:
```
virsh net-define internalbridge.xml
virsh net-autostart internal
virsh net-start intbridge
virsh net-list --all
virsh ned-destroy somebridge
```

IP forwarding
```
vi /etc/sysctl.conf
net.ipv4.ip_forward = 1
sysctl -p
```

Attach VM to network:
```
virsh attach-interface --domain server --type network --source intbridge --model virtio --config --live
virsh domiflist server
virsh detach-interface --domain server --type network --mac aa:bb:cc:dd:ee:ff --config --live
```

### Add disk

Make a new disk:
```
qemu-img create -f raw /var/lib/libvirt/images/newdisk.img 10G
```

Attach the disk
```
virsh attach-disk server --source /var/.../newdisk.img --target vdb --persistent
```

In the VM, format and mount the new disk:
```
lsblk
sfdisk << EOF # two partitions
0
1024
EOF
mkfs.ext4 /dev/vdb1
mkfs.xfs /dev/vdb2
```

Detach the disk:
```
virsh detach-disk --domain server --target vdb --persistent
```


