# -*- coding: utf-8 -*-

__author__ = "Piotr Kandziora <raveenpl@gmail.com>"

import json

from pyoecli.ssh import execute_command


class CommandError(Exception):
    """ CommandError Exception """


def JSON_handler(func):
    """ 
    Decorator. Handles output from SSH command. 
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
    _cmd = "get_pools --json"
    return execute_command(_cmd)


@JSON_handler
def get_volumes_for_given_pool(pool):
    _cmd = "get_volumes_for_given_pool --json --pool %s" % (pool)
    return execute_command(_cmd)


@JSON_handler
def get_snapshots_for_given_volume(pool, volume):
    _cmd = "get_snapshots_for_given_volume --json \
                    --pool %s --volume %s" % (pool, volume)
    return execute_command(_cmd)


@JSON_handler
def get_clones_for_given_snapshot(pool, volume, snapshot):
    _cmd = "get_clones_for_given_snapshot --json --pool %s --volume %s \
                            --snapshot %s" % (pool, volume, snapshot)
    return execute_command(_cmd)


@JSON_handler
def get_iscsi_targets_for_given_pool(pool):
    _cmd = "get_iscsi_targets_for_given_pool --json --pool %s" % (pool)
    return execute_command(_cmd)


@JSON_handler
def get_volumes_assigned_to_iscsi_target(pool, target):
    _cmd = "get_volumes_assigned_to_iscsi_target --json \
                            --pool %s --target %s" % (pool, target)
    return execute_command(_cmd)


@JSON_handler
def delete_clone(pool, volume, snapshot, clone):
    _cmd = "delete_clone --json \
            --pool %s --volume %s \
            --snapshot %s --clone %s" % (pool, volume, snapshot, clone)
    return execute_command(_cmd)


@JSON_handler
def delete_iscsi_target(pool, target):
    _cmd = "delete_iscsi_target --json --pool %s --target %s" % (pool, target)
    return execute_command(_cmd)


@JSON_handler
def delete_pool(pool):
    _cmd = "delete_pool --json --pool %s" % (pool)
    return execute_command(_cmd)


@JSON_handler
def delete_snapshot(pool, volume, snapshot):
    _cmd = "delete_snapshot --json \
            --pool %s --volume %s --snapshot %s" % (pool, volume, snapshot)
    return execute_command(_cmd)


@JSON_handler
def delete_volume(pool, volume):
    _cmd = "delete_volume --json --pool %s --volume %s" % (pool, volume)
    return execute_command(_cmd)


@JSON_handler
def detach_volume_from_iscsi_target(pool, volume, target):
    _cmd = "detach_volume_from_iscsi_target --json \
            --pool %s --volume %s --target %s" % (pool, volume, target)
    return execute_command(_cmd)


@JSON_handler
def create_iscsi_target(pool, target):
    _cmd = "create_iscsi_target --json --pool %s --target %s" % (pool, target)
    return execute_command(_cmd)


@JSON_handler
def create_clone_for_given_snapshot(pool, volume, snapshot, clone):
    _cmd = "create_clone_for_given_snapshot --json \
            --pool %s --volume %s \
            --snapshot %s --clone %s" % (pool, volume, snapshot, clone)
    return execute_command(_cmd)


@JSON_handler
def create_snapshot(pool, volume, snapshot):
    _cmd = "create_snapshot --json \
            --pool %s --volume %s --snapshot %s" % (pool, volume, snapshot)
    return execute_command(_cmd)


@JSON_handler
def create_volume(pool, volume, size,
                blocksize="131072", thin_provisioning=False,
                deduplication="off", compression="lz4", sync="always",
                logbias="latency", primary_cache="all", secondary_cache="all",
                copies="1"):

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
    _cmd = "reboot --yes"
    return execute_command(_cmd)


@JSON_handler
def shutdown():
    _cmd = "shutdown --yes"
    return execute_command(_cmd)

