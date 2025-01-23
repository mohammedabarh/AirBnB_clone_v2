#!/usr/bin/python3
from fabric.api import env
from fabric.operations import local
from fabric.contrib.files import exists

env.hosts = ['<IP_web_01>', '<IP_web_02>']

def deploy():
    """Creates and distributes an archive to your web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
