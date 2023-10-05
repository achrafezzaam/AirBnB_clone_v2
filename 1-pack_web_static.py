#!/usr/bin/python3
''' Create an archive from the web_static content '''
from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    ''' Create a .tgz from the content of the web_static folder '''
    local("mkdir -p versions")
    filepath = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    check_file = local("tar -cvzf {} web_static".format(path))

    if check_file.failed:
        return None
    return filepath
