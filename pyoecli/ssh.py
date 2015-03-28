# -*- coding: utf-8 -*-

__author__ = "Piotr Kandziora <raveenpl@gmail.com>"

import ConfigParser
import socket
import paramiko


SSH_TIMEOUT = 10
CREDENTIALS_CONFIG = "/etc/oecli/ssh.conf"


class CommunicationError(Exception):
    CMD_ERROR = 1
    CONNECTION_PROBLEM = 2
    AUTHENTICATION_PROBLEM = 3
    CONF_MISMATCH = 4


class SSHClient(object):
    """
    Class representing SSH cli connection.
    """
    def __init__(self, hostname, port, username, 
                    password=None, key_filename=None):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.key_filename = key_filename

    def execute(self, command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.hostname, 
                    port=self.port, 
                    username=self.username, 
                    password=self.password,
                    key_filename=self.key_filename,
                    timeout = SSH_TIMEOUT)
        except socket.error:
            raise CommunicationError("Connection problem.", 
                    CommunicationError.CONNECTION_PROBLEM)
        except paramiko.AuthenticationException:
            raise CommunicationError("Authentication problem.", 
                    CommunicationError.AUTHENTICATION_PROBLEM)
        stdin, stdout, stderr = ssh.exec_command(command)
        exit_code = stderr.channel.recv_exit_status()
        if exit_code != 0:
            stderr_output = stderr.channel.recv(65535)
            raise CommunicationError(stderr_output, CommunicationError.CMD_ERROR)
        stdout_output = stdout.channel.recv(65535)
        return stdout_output


def get_ssh_credentials(config_name=CREDENTIALS_CONFIG):
    """
    Gets credentials data from config.

    Args:
        config_name: config to load.

    Returns:
        dict: credentials data.
    """

    credentials = {}
    config = ConfigParser.ConfigParser()
    config.read(CREDENTIALS_CONFIG)

    try:
        credentials["address"] = config.get("credentials", "address").strip("\"")
        credentials["port"] = int(config.get("credentials", "port").strip("\""))
        credentials["username"] = config.get("credentials", "username").strip("\"")

        password = config.get("credentials", "password").strip("\"")
        if password == "":
            password = None
        credentials["password"] = password

        key_filename = config.get("credentials", "key_filename").strip("\"")
        if key_filename == "":
            key_filename = None
        credentials["key_filename"] = key_filename

    except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
        raise CommunicationError("Mismatch configuration.",
                CommunicationError.CONF_MISMATCH)
    return credentials


def execute_command(command):
    """
    Executes SSH command.

    Args:
        command: command to execute

    Returns:
        str: command output
    """

    credentials = get_ssh_credentials()
    ssh_cli = SSHClient(credentials["address"],
                        credentials["port"],
                        credentials["username"],
                        credentials["password"],
                        credentials["key_filename"])
    return ssh_cli.execute(command)
