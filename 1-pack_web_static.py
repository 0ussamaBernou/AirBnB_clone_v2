#!/usr/bin/python3
from fabric.api import local
import datetime

# Get current datetime object
now = datetime.datetime.now()


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder of the AirBnB Clone repo
    """

    local("mkdir -p ./versions")
    archive = f"./versions/web_static_{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}.tgz"
    code = local(
        f"tar -cvzf {archive} /data/web_static",
        capture=True,
    )

    return (archive) if code == 0 else None
