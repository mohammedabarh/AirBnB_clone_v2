#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers.

Execute the script using:
fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

# Define the remote hosts for deployment
env.hosts = ['54.164.253.166', '52.204.144.35']


def do_pack():
    """Generates a tgz archive from the web_static folder."""
    try:
        # Create a timestamp for the archive filename
        date = datetime.now().strftime("%Y%m%d%H%M%S")

        # Create a versions directory if it does not exist
        if isdir("versions") is False:
            local("mkdir versions")

        # Define the archive file name
        file_name = "versions/web_static_{}.tgz".format(date)

        # Create the tar.gz archive of the web_static folder
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        # Log any exceptions and return None
        print("Error creating archive: {}".format(e))
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    # Check if the archive exists
    if exists(archive_path) is False:
        return False
    try:
        # Extract the filename and name without the extension
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload the archive to the temporary directory
        put(archive_path, '/tmp/')

        # Create a new directory for the release
        run('mkdir -p {}{}/'.format(path, no_ext))

        # Unpack the archive in the new directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))

        # Remove the archive from the temporary directory
        run('rm /tmp/{}'.format(file_n))

        # Move the contents of web_static to the release directory
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))

        # Remove the now-empty web_static directory
        run('rm -rf {}{}/web_static'.format(path, no_ext))

        # Remove the current symlink
        run('rm -rf /data/web_static/current')

        # Create a new symlink to the latest release
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        # Log any exceptions and return False
        print("Error during deployment: {}".format(e))
        return False


def deploy():
    """Creates and distributes an archive to the web servers."""
    # Create an archive
    archive_path = do_pack()
    if archive_path is None:
        return False

    # Deploy the created archive
    return do_deploy(archive_path)
