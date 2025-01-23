#!/usr/bin/python3
# 1-pack_web_static.py

from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        # Create versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate archive name using current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"versions/web_static_{timestamp}.tgz"

        # Create the archive
        local(f"tar -cvzf {archive_name} web_static")

        return archive_name
    except Exception:
        return None
