#!/usr/bin/python3
from fabric.api import env, put, run
import os

env.hosts = ['<IP_web_01>', '<IP_web_02>']

def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory
        put(archive_path, '/tmp/')
        
        # Get the filename without the extension
        filename = archive_path.split('/')[-1]
        no_ext = filename.split('.')[0]
        
        # Create the release directory
        run(f"mkdir -p /data/web_static/releases/{no_ext}/")
        
        # Uncompress the archive
        run(f"tar -xzf /tmp/{filename} -C /data/web_static/releases/{no_ext}/")
        run(f"rm /tmp/{filename}")  # Delete the archive from the server
        
        # Move files to the correct directory
        run(f"mv /data/web_static/releases/{no_ext}/web_static/* /data/web_static/releases/{no_ext}/")
        run(f"rm -rf /data/web_static/releases/{no_ext}/web_static")  # Remove the unneeded folder
        
        # Delete the current symbolic link
        run("rm -rf /data/web_static/current")
        
        # Create a new symbolic link
        run(f"ln -s /data/web_static/releases/{no_ext}/ /data/web_static/current")
        
        return True
    except Exception:
        return False
