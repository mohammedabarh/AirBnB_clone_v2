#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of web_static
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Creates a compressed archive of the web_static folder
    """
    try:
        # Create versions directory if it doesn't exist
        local("mkdir -p versions")
        
        # Generate archive name using current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        
        # Create archive from web_static folder
        local("tar -cvzf {} web_static".format(archive_path))
        
        # Return archive path if successful
        if os.path.exists(archive_path):
            return archive_path
    except:
        return None
