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
    return (
        local(
            f"tar -cvzf ./versions/web_static_{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}.tgz /data/web_static/",
            capture=True,
        )
    ) or None
