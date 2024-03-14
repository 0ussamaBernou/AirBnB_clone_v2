#!/usr/bin/python3
from fabric.api import local, task
import datetime

# Get current datetime object
now = datetime.datetime.now()


@task
def do_pack():
    """
    Generates a .tgz archive from the contents of
    the web_static folder of the AirBnB Clone repo
    """

    local("mkdir -p ./versions")
    time = f"{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}"
    archive = f"versions/web_static_{time}.tgz"
    code = local(
        f"tar -cvzf {archive} web_static",
        capture=True,
    )

    return (archive) if code == 0 else None
