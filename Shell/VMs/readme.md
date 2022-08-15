# Build VMs

## Make and manage a Qcow image

```
qemu-img create -f qcow2 ubuntu.qcow2 10G
qemu-img resize ubuntu.qcow2 +1G
qemu-img info ubuntu.qcow2
qemu-img snapshot -c ubuntu_snapshot_yyyy_mm_dd ubuntu.qcow2
qemu-img snapshot -l ubuntu.qcow2
qemu-img snapshot -a 1 ubuntu.qcow2
qemu-img snapshot -d ubuntu_snapshot_yyyy_mm_dd
```

## Install an OS on the Qcow image

Install an iso on the image:
```
qemu-system-x86_64 \
-m 4096\
-hda ~/myVms/ubuntu.qcow2  \
-cdrom ~/iso/Ubuntu20.04.iso \
```


