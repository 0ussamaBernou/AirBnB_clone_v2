#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""
import os
from fabric.api import env, put, run, task

# Replace with IP addresses of your web servers
env.hosts = [
    "web-01.bernoussama.tech",
    "web-02.bernoussama.tech",
]
# Replace with the username for accessing your web servers
env.user = "ubuntu"


@task(hosts=env.hosts)
def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.splitext(archive_path)[0]
        destination = f"/data/web_static/releases/{archive_name}"

        put(archive_path, "/tmp/")
        run(f"mkdir -p {destination}")
        run(f"tar -xzf /tmp/{archive_name}.tgz -C {destination} ")
        run(f"rm /tmp/{archive_name}.tgz")
        run(f"mv {destination}/web_static/* {destination}")
        run(f"rm -rf {destination}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {destination} /data/web_static/current")

        return True
    except Exception:
        return False
