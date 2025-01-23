#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""
from fabric.api import env, put, run
import os

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with your server IPs


def do_deploy(archive_path):
    """
    Deploys archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Get filename and folder name
        file_name = os.path.basename(archive_path)
        folder_name = file_name.replace('.tgz', '')
        
        # Upload archive to /tmp/
        put(archive_path, '/tmp/')
        
        # Create release directory
        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        
        # Extract archive
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            file_name, folder_name))
        
        # Remove archive
        run('rm /tmp/{}'.format(file_name))
        
        # Move files to proper location
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(folder_name, folder_name))
        
        # Remove extra web_static directory
        run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))
        
        # Remove old current symlink
        run('rm -rf /data/web_static/current')
        
        # Create new symlink
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(
            folder_name))
        
        return True
    except:
        return False
