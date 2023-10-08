#!/usr/bin/python3
'''  Create an archive and it distribute it to the web servers '''
import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.user = 'ubuntu'
env.hosts = ['54.144.197.160', '100.26.218.107']


@runs_once
def do_pack():
    ''' Create a .tgz from the content of the web_static folder '''
    local("mkdir -p versions")
    filepath = ("versions/web_static_{}.tgz"
                .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    check_file = local("tar -cvzf {} web_static".format(filepath))

    if check_file.failed:
        return None
    return filepath


def do_deploy(archive_path):
    ''' Distribute an archive to the webservers '''
    if not os.path.exists(archive_path):
        return False
    file = os.path.basename(archive_path)
    folder_name = file.replace(".tgz", "")
    folder = "/data/web_static/releases/{}/".format(folder_name)
    try:
        put(archive_path, "/tmp/{}".format(file))
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm -rf /tmp/{}".format(file))
        run("mv {}web_static/* {}".format(folder, folder))
        run("rm -rf {}web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
    except Exception:
        return False
    return True


def deploy():
    '''
        Make a call to the do_pack and do_deploy to pack
        local files and deploy them
    '''
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    return False
