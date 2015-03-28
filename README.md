# pyoecli
Open-E JovianDSS CLI Python bindings

Simple Python library (unofficial) for managing Open-E JovianDSS via CLI service.

From Open-E website (http://open-e.com):

*Open-E JovianDSS is a ZFS- and Linux-based Data Storage Software designed especially for enterprise-sized storage environments. With its unique features, the product ensures highest data reliability and integrity. It addresses the needs of enterprise users seeking a unified NAS and SAN solution with thin provisioning, compression and deduplication.*

## Requirements
* JovianDSS with enabled CLI service.

## Installation

```
git clone https://github.com/raveenpl/pyoecli.git
```

```
pyoecli# python setup.py install
```

## Configuration
Configure authorization settings in /etc/oecli/ssh.conf. Data to fill: address, port, username, password or key_file. 

**Note**: Ensure that authorization settings file is read protected so only administrator is able to view it.

## Code Sample

```
from pyoecli import commands
print commands.get_pools()
```

Example output:

```
{
  u'data': [
    {
      u'status': 24,
      u'name': u'Pool-0',
      u'scan': None,
      u'read': u'0',
      u'iostats': {
        u'read': u'0',
        u'write': u'0',
        u'chksum': u'0'
      },
      u'vdevs': [
        {
          u'name': u'scsi-0QEMU_QEMU_HARDDISK_drive-scsi0-0-1',
          u'iostats': {
            u'read': u'0',
            u'write': u'0',
            u'chksum': u'0'
          },
          u'disks': [
            {
              u'led': u'off',
              u'name': u'sdb',
              u'iostats': {
                u'read': u'0',
                u'write': u'0',
                u'chksum': u'0'
              },
              u'class': u'Disk',
              u'health': u'ONLINE',
              u'sn': u'',
              u'path': u'pci-0000:00:05.0-scsi-0:0:1:0',
              u'model': u'QEMU HARDDISK   ',
              u'id': u'scsi-0QEMU_QEMU_HARDDISK_drive-scsi0-0-1',
              u'size': 10737418240
            }
          ],
          u'health': u'ONLINE',
          u'vdev_replacings': [
            
          ],
          u'vdev_spares': [
            
          ],
          u'type': u'',
          u'class': u'Vdev'
        }
      ],
      u'write': u'0',
      u'health': u'ONLINE',
      u'chksum': u'0',
      u'operation': u'none',
      u'class': u'Zpool'
    }
  ],
  u'error': None
}
```
