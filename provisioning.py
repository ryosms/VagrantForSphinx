from fabric.api import sudo


def pip():
    sudo("apt-get install -y make")
    sudo("apt-get install -y python-pip")


def sphinx():
    sudo("pip install sphinx")
    sudo("pip install sphinxtogithub")
    sudo("pip install sphinx-bootstrap-theme")


def init():
    pip()
    sphinx()
