# -*- coding: utf-8 -*-

__author__ = "Piotr Kandziora <raveenpl@gmail.com>"

import json

from pyoecli.ssh import execute_command


class CommandError(Exception):
    """ CommandError Exception """


def JSON_handler(func):
    """ 
    Decorator.

    Handles output from SSH command.
    Translates server error to local exception (CommandError).
    """

    def func_wrapper(*args):
        output = json.loads(func(*args))
        if output['error']:
            raise CommandError(output['error'])
        return output
    return func_wrapper


@JSON_handler
def attach_volume_to_iscsi_target(pool, volume, target,
                                scsiid=None, lun=None, mode=None):
    """
    Attaches volume (zvol) to iSCSI Target.

    :param pool:        Pool name.
    :param volume:      Volume name.
    :param target:      iSCSI Target name
    :param scsiid:      SCSIID for volume
    :param lun:         LUN number
    :param mode:        Mode. Values: rw, ro.
    """

    _cmd = "attach_volume_to_iscsi_target --json \
                --pool %s --volume %s --target %s" % (pool, volume, target)
    if scsiid:
        _cmd += " --scsiid %s" % (scsiid)
    if lun:
        _cmd += " --lun %s" % (lun)
    if mode:
        _cmd += " --mode %s" % (mode)
    return execute_command(_cmd)


@JSON_handler
def get_pools():
    """
    Returns all pools (zpool) from the system.
    """

    _cmd = "get_pools --json"
    return execute_command(_cmd)


@JSON_handler
def get_volumes_for_given_pool(pool):
    """
    Returns volumes (zvols) created on given pool.

    :param pool:        Pool name.
    """

    _cmd = "get_volumes_for_given_pool --json --pool %s" % (pool)
    return execute_command(_cmd)


@JSON_handler
def get_snapshots_for_given_volume(pool, volume):
    """
    Returns all snapshots associated with given volume.

    :param pool:        Pool name.
    :param volume:      Volume name.
    """

    _cmd = "get_snapshots_for_given_volume --json \
                    --pool %s --volume %s" % (pool, volume)
    return execute_command(_cmd)


@JSON_handler
def get_clones_for_given_snapshot(pool, volume, snapshot):
    """
    Returns all clones associated with given snapshot.

    :param pool:        Pool name.
    :param volume:      Volume name.
    :param snapshot:    Snapshot name.
    """

    _cmd = "get_clones_for_given_snapshot --json --pool %s --volume %s \
                            --snapshot %s" % (pool, volume, snapshot)
    return execute_command(_cmd)


@JSON_handler
def get_iscsi_targets_for_given_pool(pool):
    """
    Returns all iSCSI Targets configured on given pool.

    :param pool:        Pool name.
    """

    _cmd = "get_iscsi_targets_for_given_pool --json --pool %s" % (pool)
    return execute_command(_cmd)


@JSON_handler
def get_volumes_assigned_to_iscsi_target(pool, target):
    """
    Returns all volumes (zvols) assigned to given iSCSI Target.

    :param pool:        Name of the pool where iSCSI Target configuration resides.
    :param target:      Name of iSCSI Target.

    """

    _cmd = "get_volumes_assigned_to_iscsi_target --json \
                            --pool %s --target %s" % (pool, target)
    return execute_command(_cmd)


@JSON_handler
def delete_clone(pool, volume, snapshot, clone):
    """
    Deletes clone.

    :param pool:        Pool name.
    :param volume:      Volume name.
    :param snapshot:    Snapshot name.
    :param clone:       Name of clone to delete.
    """

    _cmd = "delete_clone --json \
            --pool %s --volume %s \
            --snapshot %s --clone %s" % (pool, volume, snapshot, clone)
    return execute_command(_cmd)


@JSON_handler
def delete_iscsi_target(pool, target):
    """
    Deletes iSCSI Target.

    :param pool:        Name of the pool where iSCSI Target configuration resides.
    :param target:      Name of iSCSI Target.
    """

    _cmd = "delete_iscsi_target --json --pool %s --target %s" % (pool, target)
    return execute_command(_cmd)


@JSON_handler
def delete_pool(pool):
    """
    Deletes pool.

    :param pool:        Name of the pool to delete.
    """

    _cmd = "delete_pool --json --pool %s" % (pool)
    return execute_command(_cmd)


@JSON_handler
def delete_snapshot(pool, volume, snapshot):
    """
    Deletes snapshot.

    :param pool:        Pool name.
    :param volume:      Volume name.
    :param snapshot:    Name of the snapshot to delete.
    """

    _cmd = "delete_snapshot --json \
            --pool %s --volume %s --snapshot %s" % (pool, volume, snapshot)
    return execute_command(_cmd)


@JSON_handler
def delete_volume(pool, volume):
    """
    Deletes volume.

    :param pool:        Pool name.
    :param volume:      Name of the volume to delete.
    """

    _cmd = "delete_volume --json --pool %s --volume %s" % (pool, volume)
    return execute_command(_cmd)


@JSON_handler
def detach_volume_from_iscsi_target(pool, volume, target):
    """
    Detaches volume from iSCSI Target.

    :param pool:        Pool name where iSCSI Target configuration is stored.
    :param volume:      Volume name to detach.
    :param target:      iSCSI Target to operate with.
    """

    _cmd = "detach_volume_from_iscsi_target --json \
            --pool %s --volume %s --target %s" % (pool, volume, target)
    return execute_command(_cmd)


@JSON_handler
def create_iscsi_target(pool, target):
    """
    Creates iSCSI Target that resides on given pool.

    :param pool:        Pool name.
    :param target:      Name of iSCSI Target to create.
    """

    _cmd = "create_iscsi_target --json --pool %s --target %s" % (pool, target)
    return execute_command(_cmd)


@JSON_handler
def create_clone_for_given_snapshot(pool, volume, snapshot, clone):
    """
    Creates clone for given snapshot.

    :param pool:        Pool name.
    :param volume:      Volume name.
    :param snapshot:    Snapshot name.
    :param clone:       Name of clone to create.
    """

    _cmd = "create_clone_for_given_snapshot --json \
            --pool %s --volume %s \
            --snapshot %s --clone %s" % (pool, volume, snapshot, clone)
    return execute_command(_cmd)


@JSON_handler
def create_snapshot(pool, volume, snapshot):
    """
    Creates snapshot.

    :param pool:        Pool name.
    :param volume:      Volume name.
    :param snapshot:    Name of snapshot to create.
    """

    _cmd = "create_snapshot --json \
            --pool %s --volume %s --snapshot %s" % (pool, volume, snapshot)
    return execute_command(_cmd)


@JSON_handler
def create_volume(pool, volume, size,
                blocksize="131072", thin_provisioning=False,
                deduplication="off", compression="lz4", sync="always",
                logbias="latency", primary_cache="all", secondary_cache="all",
                copies="1"):
    """
    Creates volume.

    :param pool:        Pool name.
    :param volume:      Name of volume to create.
    :param size:        Volume size in KiB or MiB or GiB or TiB.
    :param blocksize:   Blocksize in bytes.
                        Values: 8192 (8 KiB); 16384 (16 KiB);
                        32768 (32 KiB); 65536 (64 KiB); 131072 (128 KiB) (default)
    :param thin_provisioning:
                        Sets thin_provisioning attribute for volume
    :param deduplication:
                        Sets deduplication property.
                        Values: off (default); on; verify; sha256; sha256,verify
    :param compression: Sets compression property.
                        Values: off; on; lzjb; gzip; gzip-1; gzip-2; gzip-3; gzip-4; gzip-5;
                        gzip-6; gzip-7; gzip-8; gzip-9; zle; lz4 (default)
    :param sync:        Sets sync property:
                        Values: always (default); standard; disabled
    :param logbias:     Sets logbias property:
                        Values: latency (default); throughput
    :param primary_cache:
                        Sets primary cache property.
                        Values: all (default); none; metadata
    :param secondary_cache:
                        Sets secondary cache property.
                        Values: all (default); none; metadata
    :param copies:      Sets copies property.
                        Values: 1 (default); 2; 3
    """

    _cmd = "create_volume --json \
            --pool %s --volume %s --size %s \
            --blocksize %s --deduplication %s --compression %s \
            --sync %s --logbias %s --primary-cache %s \
            --secondary-cache %s --copies %s" % (pool, volume, size,
                                                blocksize, deduplication, compression,
                                                sync, logbias, primary_cache,
                                                secondary_cache, copies)
    if thin_provisioning:
        _cmd += " --thin-provisioning"
    return execute_command(_cmd)


@JSON_handler
def reboot():
    """
    Reboot server.
    """
    _cmd = "reboot --yes"
    return execute_command(_cmd)


@JSON_handler
def shutdown():
    """
    Shutdown server.
    """
    _cmd = "shutdown --yes"
    return execute_command(_cmd)


@JSON_handler
def create_pool(pool, vdevs, vdevs_mirror_multiple_group=False,
                write_log=None, read_cache=None, spare=None):
    """
    Creates pool.

    :param pool:        Name of pool to create.
    :param vdevs:       Pool vdevs definition.
                        Format: "TYPE:DISK1,DISK2;TYPE:DISK3,DISK4"
                        TYPE values: single; mirror; raidz1; raidz2; raidz3
                        Example: "single:sdg;raidz1:sdb,sdc,sdd"
    :param vdevs_mirror_multiple_group:
                        Use multiple mirror group
    :param write_log:   Write log group
                        Format: "TYPE:DISK1,DISK2"
                        TYPE values: single; mirror
    :param read_cache:  Add read cache
                        Format: "DISK1,DISK2, DISK3"
    :param spare:       Add spare disks
                        Format: "DISK1,DISK2,DISK3"
    """

    _cmd = "create_pool --json --pool %s --vdevs %s" % (pool, vdevs)
    if vdevs_mirror_multiple_group:
        _cmd += "  --vdevs-mirror-multiple-group"
    if write_log:
        _cmd += " --write-log %s" % (write_log)
    if read_cache:
        _cmd += " --read-cache %s" % (read_cache)
    if spare:
        _cmd += " --spare %s" % (spare)
    return execute_command(_cmd)
