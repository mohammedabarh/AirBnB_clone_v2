#!/usr/bin/python3
# 2-do_deploy_web_static.py

from fabric.api import env, put, run
import os

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual IPs

def do_deploy(archive_path):
    """Deploys the archive to the web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/
        put(archive_path, "/tmp/")

        # Extract the archive filename without extension
        archive_name = os.path.basename(archive_path)
        release_folder = f"/data/web_static/releases/{archive_name.split('.')[0]}"

        # Create the release folder
        run(f"mkdir -p {release_folder}")

        # Uncompress the archive
        run(f"tar -xzf /tmp/{archive_name} -C {release_folder}")

        # Delete the archive from /tmp/
        run(f"rm /tmp/{archive_name}")

        # Move contents to the release folder
        run(f"mv {release_folder}/web_static/* {release_folder}/")

        # Remove the empty web_static folder
        run(f"rm -rf {release_folder}/web_static")

        # Update the symbolic link
        run("rm -rf /data/web_static/current")
        run(f"ln -s {release_folder} /data/web_static/current")

        return True
    except Exception:
        return False
