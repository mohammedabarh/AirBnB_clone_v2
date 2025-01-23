#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    if not os.path.exists("versions"):
        local("mkdir versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{timestamp}.tgz"

    local(f"tar -cvzf {archive_path} web_static")

    return archive_path if os.path.exists(archive_path) else None
